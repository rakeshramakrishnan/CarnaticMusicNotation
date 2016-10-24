from MIDIread import *
from Note import *
from Raagam import *

RaagamObj = Raagam('Mohanam', 28)
filename = 'raghuvamsa4.mid'
MIDI_note_dict_list = []
MIDI_note_dict_list = MIDIToNoteList(filename)

note_list = []

for i in MIDI_note_dict_list:
    notetemp = Note.MIDIToSwaram(i, RaagamObj)
    note_list.append(notetemp)
    

