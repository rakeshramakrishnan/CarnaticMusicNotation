import midi
''' In this script, we will write the list of Note objects as a MIDI file. '''

def NoteListToMIDI(filename, note_list, num_aksharam, swaras_per_aksharam):
    # pattern = midi.read_midifile(filename)
    
    MIDI_note_list = []
    MIDI_note_list.append(midi.TrackNameEvent(tick = 0, text = 'Rakesh', data = [70, 76, 32, 75, 101, 121, 115, 32, 49]))
    
    for i in note_list:
        event = midi.NoteOnEvent(tick = 0, channel = 0, data = [i.MIDINote, 100])
        MIDI_note_list.append(event)
        event = midi.NoteOffEvent(tick = int(24*i.NoteLength), channel = 0, data = [i.MIDINote, 100])
        MIDI_note_list.append(event)
      
    MIDI_note_list.append(midi.EndOfTrackEvent(tick=0, data = []))
    
    songpattern = midi.Pattern(format = 1, resolution = 96, tracks = \
    [midi.Track([midi.SetTempoEvent(tick = 0, data = [12, 53, 0]),
    midi.TimeSignatureEvent(tick=0, data=[num_aksharam, swaras_per_aksharam/2, 24, 8]), midi.EndOfTrackEvent(tick=0, data = [])]),
    midi.Track(MIDI_note_list)])
    
    midi.write_midifile(filename, songpattern)
    