#!usr/bin/env python
import numpy as np
from scipy.stats import norm
import requests

all_chords = []

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

"""Assume data passed in as numpy array"""
def find_delta(data):
	delta = data[1:] - data[:-1]
	top = max(np.abs(delta.max()), np.abs(delta.min()))
	delta = delta / top * 15

def get_chord_probs(previous_chords):
	payload = {'cp':','.join(map(str, previous_chords))}
	chords = requests.get('http://www.hooktheory.com/api/trends/stats', params=payload).json()
	probs = {chord['chord_ID'] : chord['probability'] for chord in chords}
	return probs

"""index = index of all_chords"""
def get_best_chord(index, previous_chords):
	chord_probs = get_chord_probs(previous_chords)
	probs = norm.pdf(np.arange(len(all_chords)), index)
	all_chord_dict = {chord : p for chord in all_chords for p in probs}
	max_prob = float('-inf')
	best_chord = None
	for chord in chord_probs:
		if chord in all_chord_dict:
			prob = chord_probs[chord] * all_chord_dict[chord]
			if prob > max_prob:
				max_prob = prob
				best_chord = chord
	return best_chord