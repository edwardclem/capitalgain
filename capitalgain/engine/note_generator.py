#!usr/bin/env python
import numpy as np
from scipy.stats import norm
import requests
from random import randint
from utils import get_data, get_delta
# 264, 26, 364 disallowed
all_chords = ['664', '66', '6', '2', '36', '3', '27', '37', '67', 'b7', '47', '57', '17', '5/5', '464', '46', '4', '564', '56', '5', '164', '16', '1']

"""Returns dict"""
def get_chord_probs(previous_chords):
	payload = {'cp':','.join(previous_chords)}
	chords = requests.get('http://www.hooktheory.com/api/trends/stats', params=payload).json()
	probs = {chord['chord_ID'] : chord['probability'] for chord in chords}
	return probs

"""Data must be normal array not numpy array, returns two normal arrays"""
def get_duration(data):
	i = 1
	count = [1]
	while i < len(data):
		if np.abs(data[i] - data[i-1]) <= 2:
			count[-1] += 1
			data.pop(i)
		else:
			i += 1
			count.append(1)
	return data, count


"""index = index of all_chords"""
def get_best_chord(index, previous_chords):
	chord_probs = get_chord_probs(previous_chords)
	probs = norm.pdf(np.arange(len(all_chords)), index)
	all_chord_dict = {chord : p for chord, p in zip(all_chords, probs)}
	max_prob = float('-inf')
	best_chord = None
	for chord in chord_probs:
		if chord in all_chord_dict:
			prob = chord_probs[chord] * all_chord_dict[chord]
			if prob > max_prob:
				max_prob = prob
				best_chord = chord
	if not best_chord: # suuuuper hacky
		best_chord = get_best_chord(index, previous_chords[-len(previous_chords) + 1:])
	return best_chord

def generate_song(filename):
	delta = get_delta(filename)
	delta = map(int, delta)
	delta, count = get_duration(delta)
	# Obtain first chord
	song = [requests.get('http://www.hooktheory.com/api/trends/stats').json()[randint(0, 10)]['chord_ID']]
	# Generate rest of song
	for datapoint in delta:
		song.append(get_best_chord(datapoint, song[-randint(1, 4):]))
		if song[-1].isdigit() and song[-1][-1] == '7' and len(song[-1]) == 2 and randint(0, 10) > 5:
			song[-1] = song[0]
		print song[-1]

	return song, count

def phil_use_this(filename):
	song, count = generate_song(filename)
	positivity = {chord_id:pos for pos, chord_id in enumerate(all_chords)}
	return [{'name':chord, 'dur':time, '+/-':positivity[chord]} for chord, time in zip(song, count)]

def fit_melody(filename):
	data = get_data(filename)
	data = data[1:]
	x = np.arange(len(data))
	p = np.polyfit(x, data, 3)
	predicted = p[0]*(x**3) + p[1]*(x**2) + p[2]*x + p[3]
	diff = data - predicted
	diff = diff - diff.min()
	diff = diff / diff.max()
	diff = diff * 23
	return diff

def generate_melody(filename, chord_data):
	diffs = fit_melody(filename)
	durations = [el['dur'] for el in chord_data]
	durations = set(np.cumsum(durations))
	for val in diffs:
		closest_pitch = int(val) # find closest pitch some other way?
		#if len(melody) / 2 in durations:
		#	closest_pitch = # find closest pitch in chord somehow
		melody.append(closest_pitch)










