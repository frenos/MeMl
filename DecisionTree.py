import math
import numpy as np
from collections import Counter
import sys

class Tree:

    def __init__(self):
        self.theta = 0.1




    def _entropy(self, data_set, feature):
        entropy = 0

        data_len = len(data_set)

        if data_len == 0:
            return None

        if data_len == 1:
            return 0

        feature_vec = data_set[:, feature]
        counter = Counter(feature_vec)
        print(counter.most_common())

        try:
            for x in counter.most_common():
                p = x[1]/data_len
                entropy += (-1) * p * math.log(p,2)
        except ValueError as e:
            print(e.message)

        return entropy


def test():
    tree = Tree()
    #trainSet = np.array([[2, 11, 1], [7, 4, -1], [7, 3, -1], [9, 5, -1], [9, 6, 1], [3, 9, 1], [3, 1, -1]])
    trainSet = np.array([[9, 1, -1], [9, 1, 1], [9, 1, 1], [9, 1, 1], [9, 1, 1], [4, 1, 1], [4, 1, 1], [4, 1, 1], [4, 1, 1], [4, 1, 1]])
    for i in range(2):
        print('entropy feature '+str(i))
        print(tree._entropy(trainSet, i))

test()


