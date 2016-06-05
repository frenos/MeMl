import random
import math
import operator
import numpy as np
from collections import Counter

class NearestNeighbors:

    def __init__(self, otherone = False):

        self.dist_function = self.euclidean_distance
        if otherone is True:
            self.dist_function = self.other_distance




    def getNeighbors(self, trainingSet, testInstance, k):
        distances = []
        length = len(testInstance) - 1

        if k % 2 == 0:
            print('k should be odd, i will add 1')
            k += 1

        for x in range(len(trainingSet)):
            dist = self.dist_function(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []

        for x in range(k):
            neighbors.append(distances[x])
        return neighbors

    def euclidean_distance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    def other_distance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    def classify(self, neighbours):
        # get the class from the neighbour
        classes = [neighbour[0][-1] for neighbour in neighbours]
        count = Counter(classes)
        return count.most_common()[0][0]

    def check(self, trainingSet, testIntance, k):
        _neighbours = self.getNeighbors(trainingSet=trainingSet, testInstance=testIntance, k=k)
        _class = self.classify(neighbours=_neighbours)
        return _class

def test():

    knn = NearestNeighbors()

    trainSet = np.array([[2, 11, 1], [7, 4, -1], [7, -2, -1], [9, 3, -1], [9, 6, 1], [3, 9, 1], [3, 1, -1]])
    testInstance = np.array([2, 8])
    k = 3

    _class = knn.check(trainSet, testInstance, k)
    print('testInstance has the class: ')
    print(_class)


test()