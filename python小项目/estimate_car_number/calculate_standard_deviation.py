import numpy as np

def calculate_standard_deviation(number):
    standard_deviation = np.std(number, ddof=1)
    standard_deviation = round(standard_deviation, 4)
    return standard_deviation