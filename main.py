import datareader
from Korpus import Korpus
import matplotlib.pyplot as plt
import pandas as pd

datareader.read()

gehenData = Korpus.gehen.get_accelZ("oberschenkel")
laufenData = Korpus.laufen.get_accelZ("oberschenkel")


print("mean gehen: %s" %(gehenData['accelZ (m/s^2)'].mean()))
print("mean laufen: %s" %(laufenData['accelZ (m/s^2)'].mean()))
print("std gehen: %s" %(gehenData['accelZ (m/s^2)'].std()))
print("std laufen: %s"%(laufenData['accelZ (m/s^2)'].std()))



mydata1 = Korpus.gehen.subjects[0].get_accelX("oberschenkel")
mydata2 = Korpus.gehen.subjects[0].get_accelY("oberschenkel")
mydata3 = Korpus.gehen.subjects[0].get_accelZ("oberschenkel")

rollmean = mydata3.rolling(window=10000, center=False).mean()

plt.plot(rollmean['Timestamp'],rollmean.iloc[:,[1]])

print(mydata3['accelZ (m/s^2)'].std())

#plt.plot(mydata1['Timestamp'],mydata1.iloc[:,[1]])
#plt.plot(mydata2['Timestamp'],mydata2.iloc[:,[1]])
#plt.plot(mydata3['Timestamp'],mydata3.iloc[:,[1]])
#plt.legend(['accelX', 'accelY', 'accelZ'], loc='upper left')
plt.show()