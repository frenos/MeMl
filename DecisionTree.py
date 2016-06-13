import math
import numpy as np
from collections import Counter
import sys

class Tree:

    def __init__(self, theta=0.1):
        self.theta = theta

    def _splitEntropy(self, *data_sets):
        entropy = 0.0
        overall_len = 0

        for data_set in data_sets:
            if data_set != []:
                overall_len += len(data_set)

        for data_set in data_sets:
            if data_set != []:
                data_set_weight = len(data_set)/overall_len
                entropy += (data_set_weight * self._entropy(data_set))

        return entropy

    def float_range(self, start, stop, step):
        counter = start

        while counter < stop:
            yield counter
            counter += step

    def _splitAttribute(self, data_set):

        step = 0.001
        max_entropy = 1.0
        best_feature = 0
        divisor = 0
        data_set_len = len(data_set)

        if data_set_len == 0:
            raise ValueError('data_set')

        feature_len = len(data_set[0])-1

        for feature in range(feature_len):
            min, max = self._min_max(data_set, feature)


            for i in self.float_range(min, max, step):
                under_xi = []
                over_equal_xi = []

                for set in data_set:
                    if(set[feature] < i):
                        under_xi.append(set)
                    else:
                        over_equal_xi.append(set)


                split_entropy = self._splitEntropy(np.array(under_xi), np.array(over_equal_xi))

                if split_entropy < max_entropy:
                    max_entropy = split_entropy
                    best_feature = feature
                    divisor = i

                if max_entropy == 0:
                    return best_feature, divisor


        print(max_entropy)

        return best_feature, divisor

    def generateTree(self, data_set, node):
        if self._entropy(data_set) < self.theta:
            class_vec = data_set[:, -1]
            counter = Counter(class_vec)
            node.set_class(counter.most_common()[0][0])
            return

        feature, divisor = self._splitAttribute(data_set)
        node.set_feature_and_divisor(feature, divisor)


        left_data_set, right_data_set = self._splitData(data_set, feature, divisor)

        if len(left_data_set) > 0:
            new_left_node = Node()
            node.set_left_node(new_left_node)
            self.generateTree(left_data_set, new_left_node)
        if len(right_data_set) > 0:
            new_right_node = Node()
            node.set_right_node(new_right_node)
            self.generateTree(right_data_set, new_right_node)


    def _splitData(self, data_set, feature, divisor):
        return data_set[5:], data_set[:5]


    def _min_max(self, data_set, feature):

        feature_vec = data_set[:, feature]

        min = feature_vec[0]
        max = feature_vec[0]

        for i in range(len(feature_vec)):
            if feature_vec[i] < min:
                min = feature_vec[i]
            if feature_vec[i] > max:
                max = feature_vec[i]

        return min, max

    def _entropy(self, data_set):
        feature_len = len(data_set[0]) - 1
        entropy = 0

        for feature in range(feature_len):
            entropy += self._featureEntropy(data_set, feature)

        return entropy / feature_len

    def _featureEntropy(self, data_set, feature):
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
                entropy += (-1) * p * math.log(p)
        except ValueError as e:
            print(e.message)

        return entropy


class Node:
    def __init__(self):
        self._left_node = None
        self._right_node = None
        self._feature = None
        self._divisor = None
        self._class = None

    def decide(self, test_instance):

        if self._left_node is None and self._right_node is None:
            return self._class

        if test_instance[self._feature] < self._divisor and self._left_node is not None:
            node = self._left_node
        elif test_instance[self._feature] >= self._divisor and self._right_node is not None:
            node = self._right_node

        return node.decide(test_instance)

    def set_class(self, _class):
        self._class = _class

    def set_right_node(self, right_node):
        assert isinstance(right_node, Node), "%r is not a Node" % right_node

        self._right_node = right_node

    def set_left_node(self, left_node):
        assert isinstance(left_node, Node), "%r is not a Node" % left_node

        self._left_node = left_node

    def set_feature_and_divisor(self, feature, divisor):
        self._feature = feature
        self._divisor = divisor

    def __str__(self):
        if self._left_node is None and self._right_node is None:
            return str(self._class)
        else:
            return "[feature: %f| divisor: %f]" % (self._feature, self._divisor)

    def print(self):
        if self._left_node is None and self._right_node is None:
            return
        else:
            print("              [feature: %d| divisor: %0.2f]         " % (self._feature, self._divisor))
            print("             /                          \                 ")
            print("          %s                             %s     " % (str(self._left_node), self._right_node))
            self._left_node.print()
            self._right_node.print()

def test():
    tree = Tree()
    #trainSet = np.array([[2, 4, 1], [7, 4, -1], [8, 4, -1], [9, 4, -1], [1, 4, 1], [8, 9, 1], [6, 9, -1]])
    trainSet = np.array([[9, 1, -1], [9, 1, -1], [9, 1, -1], [9, 1, -1], [9, 1, -1], [4, 1, 1], [4, 1, 1], [4, 1, 1], [4, 1, 1], [4, 1, 1]])
    '''
    for i in range(2):
        print('entropy feature %d = %f' % (i, tree._featureEntropy(trainSet, i)))

    print('entropy feature %d = %f' % (i, tree._entropy(trainSet)))

    print('entropy = %f' % (tree._splitEntropy(trainSet[:4],trainSet[4:])))

    print('best feature = %d and divisor = %d' % tree._splitAttribute(trainSet))
    '''

    root = Node()
    tree.generateTree(trainSet, root)
    print('class of the instance is %d' % root.decide(np.array([4, 1])))
    root.print()


test()


