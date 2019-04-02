import numpy as np

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_time):
        self.times.extend(list_of_time)

    def average(self):
        if type(self.times[0]) == str:
            float_times = [float(sanitize(i)) for i in self.times]
            return np.mean(float_times)
        else:
            return np.mean([sanitize(i) for i in self.times])


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs