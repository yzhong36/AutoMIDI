import sys, os
import numpy as np
import pickle
import glob
from music21 import *
from midi2audio import FluidSynth

def multi_gen(midiFile):
    notes = midiFile
    # transfer sequence numbers to notes
    boundary = int(len(transfer_dic) / 2)
    pred_nums = [x * boundary + boundary for x in predictions[0]]
    notes = [key for key in transfer_dic]
    pred_notes = [notes[int(x)] for x in pred_nums]
    
    offset = 0
    p = stream.Part()
    p.insert(instrument)
    m1p = stream.Measure()
    # create note and chord objects based on the values generated by the model
    for pattern in pred_notes:
        # rest
        if pattern == 'R':
            m1p.append(note.Rest())
        # chord
        elif ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(current_note)
                notes.append(new_note)
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            m1p.append(new_chord)
        # note
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            m1p.append(new_note)
        # increase offset each iteration so that notes do not stack
        offset += note_interval
    p.append(m1p)
    return p
