import datareader
from Korpus import Korpus
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Perceptron import Perceptron
from KNN import NearestNeighbors

datareader.read()


def generate_statistics(check_function, weight, testdata_class1, testdata_class2):
    TP = 0  # true positive
    FP = 0  # false positive
    for dataset in testdata_class1:

        classedvalue = check_function(weight, dataset)
        if classedvalue is True:
            TP = TP + 1
        else:
            FP = FP + 1

    TN = 0  # true negative
    FN = 0  # false negative

    for dataset in testdata_class2:
        classedvalue = check_function(weight, dataset)
        if classedvalue is True:
            TN = TN + 1
        else:
            FN = FN + 1

    print("TP: %d, FP: %d, TN: %d, FN: %d" % (TP, FP, TN, FN))
    return TP,FP,TN,FN

def plot_merkmal():
    stehenData = Korpus.stehen.subjects[0].get_accelX("oberschenkel")
    gehenData = Korpus.gehen.subjects[0].get_accelX("oberschenkel")
    treppeData = Korpus.treppe.subjects[0].get_accelX("oberschenkel")
    rueckwData = Korpus.rueckw.subjects[0].get_accelX("oberschenkel")

    #100 sek window
    stehenstd = stehenData.rolling(window=120, center=False).std()
    gehenstd = gehenData.rolling(window=120, center=False).std()
    treppestd = treppeData.rolling(window=120, center=False).std()
    rueckwstd = rueckwData.rolling(window=120, center=False).std()

    plt.plot(stehenstd.iloc[:,[1]])
    plt.plot(gehenstd.iloc[:,[1]])
    plt.plot(treppestd.iloc[:,[1]])
    plt.plot(rueckwstd.iloc[:, [1]])

    plt.legend(['stehen', 'gehen', 'treppe', 'rueckw'], loc='lower right')
    plt.show()


def statistiken():
    stehenData = Korpus.stehen.get_accelZ("oberschenkel")
    gehenData = Korpus.gehen.get_accelZ("oberschenkel")

    gesamtlaengeGehen = len(gehenData)
    gesamtlaengeStehen = len(stehenData)

    print("Laengen: gehen: %fs, stehen: %fs" %(gesamtlaengeGehen/60, gesamtlaengeStehen/60))

    print("mean gehen: %s" % (gehenData['accelZ (m/s^2)'].mean()))
    print("mean stehen: %s" % (stehenData['accelZ (m/s^2)'].mean()))
    print("std gehen: %s" % (gehenData['accelZ (m/s^2)'].std()))
    print("std stehen: %s" % (stehenData['accelZ (m/s^2)'].std()))


statistiken()
#plot_merkmal()


'''
Stehen ist 1, gehen ist -1
'''

stehenData = Korpus.stehen.get_accelZ("oberschenkel")['accelZ (m/s^2)'].rolling(window=2000, center=False).mean()
stehenData2 = Korpus.stehen.get_accelZ("oberschenkel")['accelZ (m/s^2)'].rolling(window=2000, center=False).std()
stehenData= stehenData[~np.isnan(stehenData)]
stehenData2 = stehenData2[~np.isnan(stehenData2)]
stehenData = np.column_stack(stehenData)
stehenData2 = np.column_stack(stehenData2)
ergebnis_line = np.full((1,stehenData.shape[1]),1)

train_data_stehen = np.concatenate((stehenData,stehenData2, ergebnis_line), axis=0)

train_data_stehen = train_data_stehen.T

# randomize all our values
np.random.shuffle(train_data_stehen)


number_of_testdata = int(np.round(len(train_data_stehen)*0.3))
# split all values in test- and train-data
test_data_stehen = train_data_stehen[:number_of_testdata]
train_data_stehen = train_data_stehen[:-number_of_testdata]



joggenData = Korpus.joggen.get_accelZ("oberschenkel")['accelZ (m/s^2)'].rolling(window=2000, center=False).mean()
joggenData= joggenData[~np.isnan(joggenData)]
joggenData = np.column_stack(joggenData)

joggenData2 = Korpus.joggen.get_accelZ("oberschenkel")['accelZ (m/s^2)'].rolling(window=2000, center=False).std()
joggenData2 = joggenData2[~np.isnan(joggenData2)]
joggenData2 = np.column_stack(joggenData2)

ergebnis_line = np.full((1, joggenData.shape[1]), -1)
train_data_joggen = np.concatenate((joggenData,joggenData2, ergebnis_line), axis=0)
train_data_joggen = train_data_joggen.T

np.random.shuffle(train_data_joggen)

number_of_testdata = int(np.round(len(train_data_joggen)*0.3))
# split all values in test- and train-data
test_data_joggen = train_data_joggen[:number_of_testdata]
train_data_joggen = train_data_joggen[:-number_of_testdata]


train_data = np.concatenate((train_data_joggen, train_data_stehen), axis=0)

#myPerceptron = Perceptron(train_data, False)
#myPerceptron.pocket(200)
#generate_statistics(myPerceptron.check,myPerceptron.weight,test_data_stehen,test_data_joggen)

#myPerceptron.plot(vec=myPerceptron.weight)
#myPerceptron.pocket(300)

myPerceptron = Perceptron(train_data, False)
myPerceptron.pla(20)
myPerceptron.plot(vec=myPerceptron.weight,save=True)
generate_statistics(myPerceptron.check,myPerceptron.weight,test_data_stehen,test_data_joggen)

myPerceptron.pocket(300)

#myKNN = NearestNeighbors(traindata=train_data)
#generate_statistics(myKNN.check,0,test_data_stehen,test_data_joggen)

print("bla")
################
#for myvalue in train_data:
#    if not myPerceptron.check_no_Weight(myvalue):
#        print("nichts klar beim pla")



#plt.plot(train_data_stehen)
#plt.plot(train_data_joggen)
#plt.show()

#mydata1 = Korpus.gehen.subjects[0].get_accelX("oberschenkel")
#mydata2 = Korpus.gehen.subjects[0].get_accelY("oberschenkel")
#mydata3 = Korpus.gehen.subjects[0].get_accelZ("oberschenkel")

#rollmean = mydata3.rolling(window=10000, center=False).mean()

#plt.plot(rollmean['Timestamp'],rollmean.iloc[:,[1]])

#print(mydata3['accelZ (m/s^2)'].std())

#plt.plot(mydata1['Timestamp'],mydata1.iloc[:,[1]])
#plt.plot(mydata2['Timestamp'],mydata2.iloc[:,[1]])
#plt.plot(mydata3['Timestamp'],mydata3.iloc[:,[1]])
#plt.legend(['accelX', 'accelY', 'accelZ'], loc='upper left')
#plt.show()