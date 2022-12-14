## Dataset
The primary dataset for training is a selection of 12 Jazz songs from [Free MIDIs](https://www.midis101.com/) and 21 Mozart classic piano songs.

### MIDI file component with mido
MIDI files holds music in form of tracks and notes as a digitial presentation. For each MIDI files, the first track(track 0) is always utitled meta message of the whole song. Usually it contains:
- track name
- time signature
- key signature
- set tempo
- multiple marker of the song structure
    - time signatures 
- end marker

Start with track 1, each track represents an instrument. In the message sequence of instrumental tracks, the first two messages are Metamessages with MIDI port (input port) and instrument details. Afterwards, the messeages marks stores the "actual" song, which can be simplified as, notes. The message can have three types:
- program change
- control change
- note 

Thoese message with notes start with a flage note_on. It contains all details of the current note:
- channel to play the sound
- tokenized note
- note velocity
- duration(time)
