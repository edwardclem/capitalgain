#!usr/bin/env python
from midiutil import MidiFile

def write_midi(cg_name):
    return

def chord_to_notes(chord,pos):
    notes = []
    theory = {['
    return notes #array of notes: bass, fifth, inversion

def write_chords(chords):
    pos = 0
    song = []
    for i in range(0,len(chords)):
        chord = chords[i]
        #get notes
        notes = chord_to_notes(chord['name'],pos)
        #add notes at pos
        song.append(notes)
        #pos += duration
        pos += chord['dur']
    return song

if __name__ == '__main__':
    testchords =[{'name':'1','dur':3},{'name':'5','dur':1},{'name':'4','dur':2}]
    print(write_chords(testchords))
