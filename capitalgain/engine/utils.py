import numpy as np

def read_data(filename):
    data = []
    with open(filename) as f:
        f.readline()
        string = f.readline()
        while (string):
            split_string = string.split(',')
            data.append(float(split_string[4]))
            string = f.readline()
    return data[-2580:]

def get_ma(values, window):
    weights = np.repeat(1.0, window) / window
    return np.convolve(values, weights, 'valid')

"""Assume data passed in as numpy array"""
def find_delta(data):
    delta = data[1:] - data[:-1]
    top = max(np.abs(delta.max()), np.abs(delta.min()))
    delta = delta / top
    return delta

def get_data(filename):
    data = read_data(filename)
    delta = find_delta(get_ma(data, 20))
    delta = delta[0::10]
    delta = delta - delta.min()
    delta = delta / max(delta) * 30
    delta = map(int, delta)
    return delta

