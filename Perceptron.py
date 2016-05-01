import numpy as np
import random

class Perceptron:
    def __init__(self, N, train_data):
        self.N = N
        self.weigth = np.zeros(self.N)

        if N != len(train_data):
            raise Exception('DUDE N != len(train_data)')

        self.X = self.parseData(train_data)

        print(self.X)

    def parseData(self, train_data):
        X = []

        ones_line = np.array([np.ones(len(train_data))])
        train_data = np.concatenate((ones_line.T, train_data), axis=1)
        result_vec = train_data[:,len(train_data):len(train_data)+1]
        train_data = train_data[:,:-1]

        for feature_vec, result in zip(train_data, result_vec):
            X.append((feature_vec, result[0]))

        return X

    def classification_error(self, weigth):
        for feature, result in self.X:
            if self.classify(weigth, feature) != result:
                return False
        return True

    def classify(self, weigth, x):
        return int(np.sign(weigth.T.dot(x)))

    def getRandoooooooomFailure(self, weigth):
        pts = self.X
        mispts = []

        for feature, result in pts:
            if self.classify(weigth,feature) != result:
                mispts.append((feature, result))

        return mispts[random.randrange(0, len(mispts))]

    def pla(self, max_iter):
        weigth = np.zeros(self.N)
        it = 0

        while it < max_iter and not self.classification_error(weigth):
            it += 1

            feature,result = self.getRandoooooooomFailure(weigth)

            weigth += result * feature

        self.weigth = weigth

        if it < max_iter:
            print('ALLET KLAR!')




train = np.array([[2,6,1], [7,4,-1], [2,6,1]])

p = Perceptron(3,train_data=train)
p.pla(10)

