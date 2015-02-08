#!usr/bin/env python
import os
from midiutil.MidiFile import *
from note_generator import phil_use_this
theory = {'1':[1,1,3,5],'4':[4,4,6,8],'6':[6,6,8,10],'5':[5,5,7,9],'2':[2,2,4,6],'3':[3,3,5,7],'27':[2,2,4,6,8],'47':[4,4,6,8,10],'67':[6,6,8,10,12],'16':[1,3,5,8],'56':[5,7,9,12],'164':[1,5,8,10],'b7':[7,7,9,11],'57':[5,5,7,9,11],'37':[3,3,5,7,9],'5/5':[5,2,4.5,6],'17':[1,1,3,5,7],'464':[4,1,4,6],'664':[6,3,6,8],'564':[5,2,5,7],'46':[4,6,8,11],'57/6':[5,3,5.5,7,9],'66':[6,1,3,6],'36':[3,5,7,10]}
MIDIOut = MIDIFile(4)

def write_midi(song,stock):
    MIDIOut.addTrackName(0,0,'Bass')
    MIDIOut.addTrackName(1,0,'Fifth')
    MIDIOut.addTrackName(2,0,'Chord')
    MIDIOut.addTrackName(3,0,'Melody')
    for t in range(0,3):
        for chord in song[t]:
            for note in chord:
                MIDIOut.addNote(t,1,note['pitch'],note['time'],note['dur'],note['vel'])
    binfile = open(stock+'.mid', 'wb')
    MIDIOut.writeFile(binfile)
    binfile.close()
    return

def pitch_to_notes(notes):
    notemap = {1:1,2:3,3:5,4:6,4.5:7,5:8,5.5:9,6:10,7:12,8:13,9:15,10:17,11:18,12:20}
    for note in notes[0]:
        print(note['pitch'])
        note['pitch'] = notemap[note['pitch']] + 24 #map to scale, repitch to C3
    for note in notes[1]:
        print(note['pitch'])
        note['pitch'] = notemap[note['pitch']] + 36 #map to scale, repitch to C3
    for note in notes[2]:
        print(note['pitch'])
        note['pitch'] = notemap[note['pitch']] + 48 #map to scale, repitch to C3
    return notes

def chord_to_notes(chord,dur,pos):
    notes = []
    print(chord + str(dur) + str(pos))
    pitches = theory[chord]
    bass = [{'pitch':(pitches[0]),'dur':dur,'time':pos,'vel':127}] #bass
    fifth = [{'pitch':(pitches[0]),'dur':dur,'time':pos,'vel':127},{'pitch':(pitches[0]+4),'dur':dur,'time':pos,'vel':127}]
    for p in range(1,len(pitches)):
        pitch = pitches[p]
        notes.append({'pitch':pitch,'dur':dur,'time':pos,'vel':127}) #chord
        p += 1
    print([bass,fifth,notes])
    return pitch_to_notes([bass,fifth,notes]) #array of notes: bass, fifth, inversion

def write_chords(chords):
    pos = 0
    song = [[],[],[]]
    for i in range(0,len(chords)):
        chord = chords[i]
        #get notes
        notes = chord_to_notes(chord['name'],chord['dur'],pos)
        #add notes at pos
        song[0].append(notes[0])
        song[1].append(notes[1])
        song[2].append(notes[2])
        pos += chord['dur']
    return song

if __name__ == '__main__':
    testchords = phil_use_this('data/aapl.us.txt')
    print(write_chords(testchords))
    write_midi(write_chords(testchords),'test')