#!usr/bin/env python
import os
from midiutil.MidiFile import MIDIFile
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
                MIDIOut.addNote(t,1,note['pitch']+36,note['time'],note['dur'],note['vel'])
    binfile = open(stock+'.mid', 'wb')
    MIDIOut.writeFile(binfile)
    binfile.close()
    return

def chord_to_notes(chord,dur,pos):
    notes = []
    print(chord + str(dur) + str(pos))
    pitches = theory[chord]
    bass = [{'pitch':(pitches[0]-16),'dur':dur,'time':pos,'vel':127}] #bass
    fifth = [{'pitch':(pitches[0]-8),'dur':dur,'time':pos,'vel':127},{'pitch':(pitches[0]-3),'dur':dur,'time':pos,'vel':127}]
    for p in range(1,len(pitches)):
        pitch = pitches[p]
        notes.append({'pitch':pitch,'dur':dur,'time':pos,'vel':127}) #chord
        p += 1
    return [bass,fifth,notes] #array of notes: bass, fifth, inversion

def write_chords(chords):
    pos = 0
    song = [[],[],[]]
    for i in range(0,len(chords)):
        chord = chords[i]
        #get notes
        #REAL ONE: notes = chord_to_notes(chord['name'],chord['dur'],pos)
        notes = chord_to_notes(chord,1,pos) #TEST ONLY
        #add notes at pos
        song[0].append(notes[0])
        song[1].append(notes[1])
        song[2].append(notes[2])
        #pos += duration
        pos += 1
    return song

if __name__ == '__main__':
    #testchords =[{'name':'1','dur':3},{'name':'5','dur':1},{'name':'4','dur':2}]
    print(write_chords(testchords))
    write_midi(write_chords(testchords),'test')