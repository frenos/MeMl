import datareader
from Korpus import Korpus

def mittelwertGesamt(daten):
    '''
    wir nehmen immer timestamp|values an.
    '''
    sum = 0
    for value in daten:
        sum += value[1]
    mittelwert = sum / len(daten)
    return mittelwert


datareader.read()

mydata = Korpus.gehen.subjects[0].get_accelX("oberschenkel")
print(mittelwertGesamt(mydata))
mydata = Korpus.joggen.subjects[0].get_accelX("oberschenkel")
print(mittelwertGesamt(mydata))
