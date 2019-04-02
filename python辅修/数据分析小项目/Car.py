import numpy as np


class Car:
    def __init__(self, brand, price, company, sales):
        self.brand = brand
        self.price = price
        self.company = company
        self.sales = sales

    def top1(self):
        time = -1
        max = 0
        for i in self.sales:
            if (max < int(i)):
                max = int(i)
                time = time + 1
        return [sorted(set([sanitize(t) for t in self.sales]))[0], time]

    def average(self):
        if type(self.sales[0]) == str:
            float_times = [float(sanitize(i)) for i in self.sales]
            return np.mean(float_times)
        else:
            return np.mean([sanitize(i) for i in self.sales])

    def best(self):
        number = 0
        time = -1
        month = []
        for i in self.sales:
            if (int(i) > 10000):
                number = number + 1
                month.append(time)
            time = time + 1
        return [number, month]

    def sort(self):
        return sorted([int(i) for i in self.sales])[0:3]


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs