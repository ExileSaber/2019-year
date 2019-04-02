import numpy as np
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]

    def add_time(self, time_value):
        self.append(time_value)

    def add_times(self, list_of_time):
        self.extend(list_of_time)

    def average(self):
        if type(self[0]) == str:
            float_times = [float(sanitize(i)) for i in self]
            return np.mean(float_times)
        else:
            return np.mean([sanitize(i) for i in self])


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs