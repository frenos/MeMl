from Subject import Subject


class Activity(object):

    def __init__(self, name, data):
        self.name = name
        self.subjects = []
        for subject in data:
            self.add_subject(subject)

    def add_subject(self, data):
        new_subject = Subject(data)
        self.subjects.append(new_subject)
