import numpy as np
from scipy.ndimage.filters import gaussian_filter1d

# Global Variables
beat_length = 10 # Controls number of data points per beat of music (original was 10)
song_length = 256 # Controls number of beats in the song (original was 256)

def read_data(filename, col=4):
    data = []
    with open(filename) as f:
        f.readline()
        string = f.readline()
        while (string):
            split_string = string.split(',')
            data.append(float(split_string[col]))
            string = f.readline()
    data = data[-(song_length*beat_length + 20):]
    if len(data) != (song_length*beat_length + 20):
        raise RuntimeWarning('Not enough data present. May cause '
            'unexpected behavior')
    return data

def get_ma(values, window):
    weights = np.repeat(1.0, window) / window
    return np.convolve(values, weights, 'valid')

"""Assume data passed in as numpy array"""
def find_delta(data):
    delta = data[1:] - data[:-1]
    top = max(np.abs(delta.max()), np.abs(delta.min()))
    delta = delta / top
    return delta

def get_std(data):
    var = np.array([np.var(data[i:i+50]) for i in range(0, len(data), beat_length/2)])
    std = var**(0.5)
    std = gaussian_filter1d(std, 10)
    std = std / std.max() * 64 + 63
    return std


def get_data(filename):
    data = read_data(filename)
    ma = get_ma(data, 20)
    return ma[::beat_length/2], get_std(ma)

def get_delta(filename):
    data = read_data(filename)
    delta = find_delta(get_ma(data, 20))
    delta = delta[::beat_length]
    delta = delta - delta.min()
    delta = delta / max(delta) * 45
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

