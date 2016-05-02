import numpy as np
import random


class Perceptron:
    def __init__(self, train_data):
        self.len_train_data = len(train_data)

        if self.len_train_data > 0:
            self.len_feature_vec = len(train_data[0])

            self.weight = np.zeros(self.len_feature_vec)

            self.X = self.parseData(train_data)

            print(self.X)
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

    def classification_error(self, weight):
        error = 0
        for feature, result in self.X:
            if self.classify(weight, feature) != result:
                error += 1
        return error

    def classify(self, weight, x):
        return int(np.sign(weight.T.dot(x)))

    def check(self, weight, x):

        x = np.concatenate((np.ones(1), x), axis=0)
        expected_result = x[self.len_feature_vec:self.len_feature_vec + 1][0]
        x = x[:-1]

        result = self.classify(weight, x)

        if expected_result == result:
            return True

        return False

    def getRandoooooooomFailure(self, weight):
        pts = self.X
        mispts = []

        for feature, result in pts:
            if self.classify(weight, feature) != result:
                mispts.append((feature, result))
        return mispts[random.randrange(0, len(mispts))]

    def pla(self, max_iter):
        weight = np.zeros(self.len_feature_vec)
        it = 0

        while it < max_iter:
            it += 1

            feature, result = self.getRandoooooooomFailure(weight)

            weight += result * feature

            error = self.classification_error(weight)

            if error == 0:
                break

        self.weight = weight

        if it < max_iter:
            print('ALLET KLAR BEIM PLA!')

    def pocket(self, max_iter):
        current_weight = np.zeros(self.len_feature_vec)
        new_weight = current_weight
        current_error = self.classification_error(current_weight)
        it = 0

        while it < max_iter:
            it += 1

            feature, result = self.getRandoooooooomFailure(current_weight)

            new_weight += result * feature

            new_error = self.classification_error(new_weight)

            if new_error < current_error:
                current_weight = new_weight
                current_error = new_error

            if current_error == 0:
                break

        self.weight = current_weight

        if it < max_iter:
            print('ALLET KLAR BEIM POCKET!')

train = np.array([[2, 6, 1], [7, 4, -1], [7, -2, -1], [7, 3, -1], [9, 6, 1], [3, 6, 1], [7, 1, -1]])

p = Perceptron(train_data=train)
p.pla(10)
print(p.weight)
p.pocket(10)
print(p.weight)
result = p.check(p.weight, np.array([7, 6, -1]))
if result is True:
    print('YOKO')

