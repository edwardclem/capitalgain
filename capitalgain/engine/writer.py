#!usr/bin/env python
from pymongo import MongoClient
from midiutil.MidiFile import *
from note_generator import phil_use_this, generate_melody

theory = {'1':[1,1,3,5],'4':[4,4,6,8],'6':[6,6,8,10],'5':[5,5,7,9],'2':[2,2,4,6],'3':[3,3,5,7],'27':[2,2,4,6,8],'47':[4,4,6,8,10],'67':[6,6,8,10,12],'16':[1,3,5,8],'56':[5,7,9,12],'164':[1,5,8,10],'b7':[7,7,9,11],'57':[5,5,7,9,11],'37':[3,3,5,7,9],'5/5':[5,2,4.5,6],'17':[1,1,3,5,7],'464':[4,1,4,6],'664':[6,3,6,8],'564':[5,2,5,7],'46':[4,6,8,11],'57/6':[5,3,5.5,7,9],'66':[6,1,3,6],'36':[3,5,7,10]}
MIDIOut = MIDIFile(4)
pitchup = 15

def write_midi(song,stock):
    MIDIOut.addTrackName(0,0,'Bass')
    MIDIOut.addTrackName(1,0,'Fifth')
    MIDIOut.addTrackName(2,0,'Chord')
    MIDIOut.addTrackName(3,0,'Melody')
    for t in range(0,4):
        for chord in song[t]:
            for note in chord:
                MIDIOut.addNote(t,1,int(note['pitch']),note['time'],note['dur'],int(note['vel']))
    binfile = open(stock+'.mid', 'wb')
    MIDIOut.writeFile(binfile)
    binfile.close()
    print('Wrote MIDI.')
    return

def pitch_to_notes(notes):
    notemap = {1:1,2:3,3:5,4:6,4.5:7,5:8,5.5:9,6:10,7:12,8:13,9:15,10:17,11:18,12:20,13:22,14:24,15:25,16:27,17:29,18:30,19:32,20:34,21:36,22:37,23:39,24:41}
    if(isinstance(notes, list)):
        for note in notes[0]:
            note['pitch'] = notemap[note['pitch']] + 2*pitchup#map to scale, repitch to C3
        for note in notes[1]:
            note['pitch'] = notemap[note['pitch']] + 3*pitchup - 3 #map to scale, repitch to C3
        for note in notes[2]:
            note['pitch'] = notemap[note['pitch']] + 4*pitchup - 1 #map to scale, repitch to C3
    else:
        notes = notemap[notes] + 4*pitchup #map to scale, repitch to C3
    return notes

def chord_to_notes(chord,dur,posit,pos):
    notes = []
    pitches = theory[chord]
    bass = [{'pitch':(pitches[0]),'dur':dur,'time':pos,'+/-':posit,'vel':127}] #bass
    fifth = [{'pitch':(pitches[0]),'dur':dur,'time':pos,'+/-':posit,'vel':127},{'pitch':(pitches[0]+4),'dur':dur,'time':pos,'vel':127}]
    for p in range(1,len(pitches)):
        pitch = pitches[p]
        notes.append({'pitch':pitch,'dur':dur,'time':pos,'+/-':posit,'vel':127}) #chord
        p += 1
    return pitch_to_notes([bass,fifth,notes]) #array of notes: bass, fifth, inversion

def write_melody(melody):
    pos = 0
    music = []  
    for note in melody:
        note['pitch'] = pitch_to_notes(note['pitch'])
        note['dur'] = 0.5
        note['time'] = pos
        song = []
        song.append(note)
        music.append(song)
        pos += 0.5
    return music

def write_chords(chords, melody):
    pos = 0
    song = [[],[],[]]
    for i in range(0,len(chords)):
        chord = chords[i]
        #get notes
        notes = chord_to_notes(chord['name'],chord['dur'],chord['+/-'],pos)
        #add notes at pos
        song[0].append(notes[0])
        song[1].append(notes[1])
        song[2].append(notes[2])
        pos += chord['dur']
    song.append(write_melody(melody))
    return song

def repack_visuals(music):
    music = [music[2],music[3]]
    return music

def send_visual(music, name):
    client = MongoClient('mongodb://cgains:moneysings@ds062097.mongolab.com:62097/capital_gain_database')
    db = client.capital_gain_database
    if db.musicdata.find_one({'ticker':name.upper()}) == None:
        visual = {'ticker':name.upper(),'file':'audio/'+name+'.mp3','musicdata':repack_visuals(music)}
        db.musicdata.insert(visual)
        print('Visual database entry created.')
    else:
        db.musicdata.update({'ticker':name.upper()},{'$set':{'musicdata':repack_visuals(music)}})
        print('Visual database entry updated.')
    return

import sys
if __name__ == '__main__':
    stock = 'aapl'
    if (len(sys.argv) == 2):
        stock = sys.argv[1]
    testchords = phil_use_this('data/' + stock + '.us.txt')
    melody = generate_melody('data/' + stock + '.us.txt', testchords)
    testmusic = write_chords(testchords, melody)
    print('Music generated.')
    write_midi(testmusic,stock)
    send_visual(testmusic,stock)