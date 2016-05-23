import numpy as np
import random
import matplotlib.pyplot as plt
import signal
import sys
import time


class Perceptron:
    def __init__(self, train_data, test):
        self.len_train_data = len(train_data)
        self.test = test
        if self.len_train_data > 0:
            self.len_feature_vec = len(train_data[0])

            self.weight = np.zeros(self.len_feature_vec)

            if test is True:
                xA, yA, xB, yB = [random.uniform(-1, 1) for i in range(4)]
                self.V = np.array([xB * yA - xA * yB, yB - yA, xA - xB])
                self.X = self.generate_points(20)
                self.test_points = self.generate_points(500)
            else:
                self.X = self.parseData(train_data)

        else:
            raise Exception('train_data with size 0')

    def parseData(self, train_data):
        X = []
        ones_line = np.array([np.ones(len(train_data))])
        train_data = np.concatenate((ones_line.T, train_data), axis=1)
        result_vec = train_data[:, self.len_feature_vec:self.len_feature_vec+1]
        train_data = train_data[:, :-1]

        for feature_vec, result in zip(train_data, result_vec):
            X.append((feature_vec, result[0]))

        return X

    def generate_points(self, N):
        X = []

        for i in range(N):
            x1, x2 = [random.uniform(-10, 10) for i in range(2)]
            x = np.array([1, x1, x2])
            s = int(np.sign(self.V.T.dot(x)))
            X.append((x, s))
        return X

    def classification_error(self, weight):
        error = 0
        for feature, result in self.X:
            if self.classify(weight, feature) != result:
                error += 1
        return error

    def classify(self, weight, x):
        value = int(np.sign(weight.T.dot(x)))
        return value

    def check_no_Weight(self,x):
        return self.check(self.weight,x)

    def check(self, weight, x):

        x = np.concatenate((np.ones(1), x), axis=0)
        expected_result = x[self.len_feature_vec:self.len_feature_vec + 1][0]
        x = x[:-1]

        result = self.classify(weight, x)

        if expected_result == result:
            return True

        return False

    def getRandomFailure(self, weight):
        pts = self.X
        mispts = []

        for feature, result in pts:
            if self.classify(weight, feature) != result:
                mispts.append((feature, result))
        return mispts[random.randrange(0, len(mispts))]

    def pla(self, max_iter):
        plt.show()
        weight = np.zeros(self.len_feature_vec)
        it = 0

        while it < max_iter:
            it += 1

            feature, result = self.getRandomFailure(weight)

            weight += result * feature
            print('Durchlauf: '+str(it))
            print(weight)
            self.plot(mispts=self.test_points,vec=weight)
            error = self.classification_error(weight)

            if error == 0:
                break

        self.weight = weight

        if it < max_iter:
            print('ALLET KLAR BEIM PLA!')

    def pocket(self, max_iter):
        current_weight = np.zeros(self.len_feature_vec)
        new_weight = current_weight.copy()
        current_error = self.classification_error(current_weight)
        it = 0

        while it < max_iter:
            it += 1

            feature, result = self.getRandomFailure(new_weight)

            new_weight =  new_weight.copy() + (result * feature)
            print('Durchlauf: ' + str(it))
            print(new_weight)
            print(current_weight)

            new_error = self.classification_error(new_weight)
            print(new_error)
            print(current_error)
            if new_error < current_error:
                current_weight = new_weight.copy()
                current_error = new_error

            if current_error == 0:
                break

        self.weight = current_weight.copy()

    def plot(self, mispts=None, vec=None, save=False):
        fig = plt.figure(figsize=(5, 5))
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)

        if self.test is True:
            V = self.V
            a, b = -V[1] / V[2], -V[0] / V[2]
            l = np.linspace(-10, 10)
            plt.plot(l, a * l + b, 'k-')

        l = np.linspace(-10, 10)
        cols = {1: 'r', -1: 'b'}
        for x, s in self.X:
            plt.plot(x[1], x[2], cols[s] + 'o')

        if mispts:
            for x, s in mispts:
                plt.plot(x[1], x[2], cols[s] + '.')

        if vec != None:
            aa, bb = -vec[1] / vec[2], -vec[0] / vec[2]
            plt.plot(l, aa * l + bb, 'g-', lw=2)

        if save:
            if not mispts:
                plt.title('N = %s' % (str(len(self.X))))
            else:
                plt.title('N = %s with %s test points' \
                          % (str(len(self.X)), str(len(mispts))))
            plt.savefig('p_N%s' % (str(len(self.X))), \
                        dpi=200, bbox_inches='tight')

        plt.draw()
        plt.pause(1)


def test1():
    print("### ERSTER TEST MIT 2"
          " MERKMALEN ###")
    train1 = np.array([[2, 11, 1], [7, 4, -1], [7, -2, -1], [9, 3, -1], [9, 6, 1], [3, 9, 1], [3, 1, -1]])
    p = Perceptron(train_data=train1, test=True)

    p.pla(10)
    print(p.weight)
    result = p.check(p.weight, np.array([9, 1, -1]))
    if result is True:
        print('TEST PLA OK\n')
    else:
        print('TEST PLA FEHLSCHLAG\n')

    p.pocket(10)
    print(p.weight)
    result = p.check(p.weight, np.array([1, 5, 1]))
    if result is True:
        print('TEST POCKET OK\n')
    else:
        print('TEST POCKET FEHLSCHLAG\n')


def test2():
    print("### ERSTER TEST MIT 1 MERKMALEN ###")
    
    train2 = np.array([[5, 1], [7, -1], [9, -1], [7, -1], [3, 1], [2, 1], [8, -1]])
    p = Perceptron(train_data=train2)

    p.pla(10)
    print(p.weight)
    result = p.check(p.weight, np.array([9, -1]))
    if result is True:
        print('TEST PLA OK\n')
    else:
        print('TEST PLA FEHLSCHLAG')

    p.pocket(10)
    print(p.weight)
    result = p.check(p.weight, np.array([1, 1]))
    if result is True:
        print('TEST POCKET OK')
    else:
        print('TEST POCKET FEHLSCHLAG')




test1()
print('YOKO')
#test2()

