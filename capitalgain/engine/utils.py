import numpy as np

def read_data(filename, col=4):
    data = []
    with open(filename) as f:
        f.readline()
        string = f.readline()
        while (string):
            split_string = string.split(',')
            data.append(float(split_string[col]))
            string = f.readline()
    data = data[-2580:]
    if len(data) != 2580:
        raise RuntimeWarning('Not enough data present. May cause '
            'unexpected behavior')
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

def get_variance(data):
    var = np.array([np.var(data[i:i+5]) for i in range(1, len(data) - 15, 5)])
    std = var**(0.5)
    std = std / std.max() * 64 + 63
    return std


def get_data(filename):
    data = read_data(filename)
    ma = get_ma(data, 20)
    return ma[0::5], get_variance(ma)

def get_delta(filename):
    data = read_data(filename)
    delta = find_delta(get_ma(data, 20))
    delta = delta[0::10]
    delta = delta - delta.min()
    delta = delta / max(delta) * 30
    return delta

try:
    import matplotlib.pyplot as plt
except ImportError:
    print 'Need matplotlib for debugging purposes'
# For debugging purposes
def visualize(data):
    x = np.arange(len(data))
    p = np.polyfit(x, data, 3)
    predicted = p[0]*(x**3) + p[1]*(x**2) + p[2]*x + p[3]
    plt.scatter(x, data)
    plt.plot(x, predicted)
    plt.show()

