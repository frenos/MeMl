import numpy as np
import os
from Korpus import Korpus

aktivitaeten = ['gehen', 'joggen', 'laufen', 'rueckw', 'stehen', 'treppe']
def read():
    datafiles = {
        'gehen' : [],
        'joggen' : [],
        'laufen' : [],
        'rueckw' : [],
        'stehen' : [],
        'treppe' : []
    }

    for file in os.listdir('./daten'):
        for activity in aktivitaeten:
            if file.startswith(activity) and not file.endswith('.ini'):
                datafiles[activity].append(np.recfromcsv('./daten/%s'%(file), names=True))

    create_Korpus(datafiles)

def create_Korpus(data):
    for activity in aktivitaeten:
        Korpus.add_activity(activity, data[activity])