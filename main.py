import datareader
from Korpus import Korpus
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Perceptron import Perceptron

datareader.read()


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

stehenData = Korpus.stehen.get_accelZ("oberschenkel")['accelZ (m/s^2)'].rolling(window=1000, center=False).mean()
stehenData= stehenData[~np.isnan(stehenData)]
stehenData = np.column_stack(stehenData)
ergebnis_line = np.full((1,stehenData.shape[1]),1)

train_data_stehen = np.concatenate((stehenData, ergebnis_line), axis=0)

train_data_stehen = train_data_stehen.T

joggenData = Korpus.joggen.get_accelZ("oberschenkel")['accelZ (m/s^2)'].rolling(window=1000, center=False).mean()
joggenData= joggenData[~np.isnan(joggenData)]
joggenData = np.column_stack(joggenData)
ergebnis_line = np.full((1, joggenData.shape[1]), -1)
train_data_joggen = np.concatenate((joggenData, ergebnis_line), axis=0)
train_data_joggen = train_data_joggen.T

train_data = np.concatenate((train_data_joggen, train_data_stehen), axis=0)

myPerceptron = Perceptron(train_data)
#myPerceptron.pla(100)
myPerceptron.pocket(300)

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