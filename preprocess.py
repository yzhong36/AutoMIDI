import numpy as np
import mido as md
import os

def read_notes(midi_file):
    '''
    read notes in midi file in a numpy array. Reading ignored metamessages
    and signature messages.

    :param midi_file: a mido object of MIDI file input
    :return notes: numpy array of notes in a midi file
    '''
    notes = np.array([])

    # skip metadata track
    tracks = midi_file.tracks
    for t in tracks:
        for m in t:
            if not m.is_meta and m.type == 'note_on':
                n = m.note
                notes = np.append(notes, n)
    return notes

def read_instruments(midi_file):
    ins = []
    tracks = midi_file.tracks
    for t in tracks:
        for m in t:
            if m.type == 'program_change':
                i = m.program
                ins += [i]
    return set(ins)

def load_midi(file_path, read_range=1, by_instrument=False):
    '''
    load the midi dataset. The function automaticaly detect whether the input
    is file or datapath. It also offers a option to read file(s) in one or by
    instruments.

    :param file_path: the file or directory to be read
    :param range: the range of files to be read in a dir. If specified when 
            reading file, nothing would change
    :by_instrument: boolean parameter to decide whether read in all or by 
            instrument
    :return notes: list of notes in midi files
    :return time: numpy array of song duration
    :return instrument: numpy array of instrument used
    '''
    # check existence
    if not os.path.exists(file_path):
        return print("file or path not found")

    notes = []
    time = np.array([])
    instruments = []

    if os.path.isfile(file_path):       
        # read a single file
        print("Reading a single song")
        print(file_path)

        song_read = md.MidiFile(file_path)
        # append time and notes
        instruments += [read_instruments(song_read)]
        time = np.append(time, song_read.length)
        notes += [read_notes(song_read)]

        return notes, time, instruments
    
    # otherwise read a dir
    print("Reading a directory")
    
    file_list = sorted(f for f in os.listdir(file_path) if not f.startswith("."))
    read_range = read_range if read_range > 1 else len(file_list) 
    
    for i in range(0,read_range):
        midi_path = file_path + file_list[i]
        print(midi_path)

        song_read = md.MidiFile(midi_path)
        # append time and notes for each song
        instruments += [read_instruments(song_read)]
        time = np.append(time, song_read.length)
        notes += [read_notes(song_read)]
        
    return notes, time, instruments

def instrument_convolution(instr_list):
    instrument_lib = ['Piano', 'Chromatic Percussion', 'Organ', 'Guitar', 'Bass',
                        'Strings', 'Ensemble', 'Brass', 'Reed', 'Pipe', 'Synth Lead',
                        'Synth Pad', 'Synth Effects', 'Ethnic', 'Percussive', 'Sound Effect' ]
    c_instr = []
    ins_count = []
    
    instr_list = np.array(instr_list).astype(int)
    instr_list = np.floor_divide(instr_list, 8)

    for i in instr_list:
        convolved_instrument = instrument_lib[i]
        if convolved_instrument not in c_instr:
            c_instr += [convolved_instrument]
    return c_instr