import numpy as np
import pandas as pd
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

    for file in sorted(os.listdir('./daten')):
        for activity in aktivitaeten:
            if file.startswith(activity) and not file.endswith('.ini'):
                datafiles[activity].append(pd.read_csv('./daten/%s'%(file)))

    create_Korpus(datafiles)

def create_Korpus(data):
    for activity in aktivitaeten:
        Korpus.add_activity(activity, data[activity])