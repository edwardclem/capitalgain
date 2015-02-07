#!usr/bin/env python
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
	return data

def get_ma(values, window):
	weights = np.repeat(1.0, window) / window
	return np.convolve(values, weights, 'valid')

