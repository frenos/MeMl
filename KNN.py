import random
import math
import operator
import numpy as np
from collections import Counter

class NearestNeighbors:

    def __init__(self, otherone = False, traindata=None):
        self.traindata = traindata
        self.dist_function = self.euclidean_distance
        if otherone is True:
            self.dist_function = self.other_distance


    def getNeighbors(self, trainingSet, testInstance, k=3):
        distances = []
        length = len(testInstance)

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

    def check(self, trainingSet, testIntance, k=3):
        _neighbours = self.getNeighbors(trainingSet=trainingSet, testInstance=testIntance, k=k)
        _class = self.classify(neighbours=_neighbours)
        return _class

    def check(self, weight, x, k=3):

        expected_result = x[-1]
        x = x[:-1]

        _neighbours = self.getNeighbors(trainingSet=self.traindata, testInstance=x, k=k)

        result = self.classify(neighbours=_neighbours)

        if expected_result == result:
            return True

        return False

def test():

    knn = NearestNeighbors(otherone=True)

    trainSet = np.array([[0.2,0.2,0.2,0.2,0.2, 1], [0.7,0.7,0.7,0.7,0.7, -1], [0.7,0.7,0.7,0.7,0.7,  -1], [0.9,0.9,0.9,0.9,0.9, -1], [0.9,0.9,0.9,0.9,0.9, 1], [0.3,0.3,0.3,0.3,0.3,0.3, 1], [0.3,0.3,0.3,0.3,0.3,0.3, -1]])
    testInstance = np.array([0.4, 0.4,0.4,0.4,0.4])
    k = 3


    _class = knn.check(trainSet, testInstance, k)
    print('testInstance has the class: ')
    print(_class)


#test()