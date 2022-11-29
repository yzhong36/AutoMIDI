

import numpy as np
import mido as md
import os

def load_midi(file_path, range=1, by_instrument=False):
    '''
    load the midi dataset. The function automaticaly detect whether the input
    is file or datapath. It also offers a option to read file(s) in all or by
    instruments.

    :param file_path: the file or directory to be read
    :param range: the range of files to be read in a dir. If specified when 
            reading file, nothing would change
    :by_instrument: boolean parameter to decide whether read in all or by 
            instrument
    :return: numpy array of midi files
    '''
    # check existence
    if not os.path.exists(file_path):
        return print("file or path not found")

    midi_data = None
    if os.path.isfile(file_path):       
        # read a single file
        print("Reading a song")
        song_read = md.MidiFile(file_path)
        return midi_data
    
    # otherwise read a dir
    print("Reading a directory")
    file_list = os.listdir(file_path)
    read_range = range if range > 1 else len(file_list) 

    for i in range(0,read_range):
        midi_file = md.MidiFile(file_list[i])
        
    return midi_data