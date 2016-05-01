from Subject import Subject
import pandas as pd

class Activity(object):

    def __init__(self, name, data):
        self.name = name
        self.subjects = []
        for subject in data:
            self.add_subject(subject)

    def add_subject(self, data):
        new_subject = Subject(data)
        self.subjects.append(new_subject)

    def get_accelX(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_accelX(sensor))
        return filtered_data

    def get_accelY(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_accelY(sensor))
        return filtered_data

    def get_accelZ(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_accelZ(sensor))
        return filtered_data

    def get_gyroX(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_gyroX(sensor))
        return filtered_data

    def get_gyroY(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_gyroY(sensor))
        return filtered_data

    def get_gyroZ(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_gyroZ(sensor))
        return filtered_data

    def get_magnetX(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_magnetX(sensor))
        return filtered_data

    def get_magnetY(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_magnetY(sensor))
        return filtered_data

    def get_magnetZ(self, sensor):
        filtered_data = pd.DataFrame()
        for subject in self.subjects:
            filtered_data = filtered_data.append(subject.get_magnetZ(sensor))
        return filtered_data
