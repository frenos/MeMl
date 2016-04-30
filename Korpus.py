from Activity import Activity


class Korpus(object):
    #Korpus enthaelt Referenzen zu allen Aktivitaeten
    activity = []
    gehen, joggen, laufen, rueckw, stehen, treppe = (None,)*6

    @staticmethod
    def add_activity(name, data):
        new_Activity = Activity(name, data)

        if name is 'gehen':
            Korpus.gehen = new_Activity
        elif name is 'joggen':
            Korpus.joggen = new_Activity
        elif name is 'laufen':
            Korpus.laufen = new_Activity
        elif name is 'rueckw':
            Korpus.rueckw = new_Activity
        elif name is 'stehen':
            Korpus.stehen = new_Activity
        elif name is ' treppe':
            Korpus.treppe = new_Activity

        Korpus.activity.append(new_Activity)
