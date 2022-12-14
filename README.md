# AutoMIDI
This project use GAN to generate Jazz music in MIDI format.

## Datasets
Please check out data/ folder and its README.md for details.

## Files

### GAN.ipynb
You can follow this notebook to explore the GANs we used to generate melody-based music.

### Preprocess.py
Preprocess method of MIDI file. It loads the midi datasetn and automaticaly decides whether the input is file or datapath. It also offers a option to read file(s) in one or by instruments. Another utility function that preprocess provides is get_details(), which returns the total time measure in ticks, ticks per beat, number of bars, lowest note value and highest note value.

### Jazzify.ipynb
The post_process notebook to turn single track model output to a multi-track Jazz music. Functions included are:

- generate_base_drum()

- generate_waling_bass()

- generate_chords_piano()

- generate_melody()

#### Final output is stored in /res/post_process
