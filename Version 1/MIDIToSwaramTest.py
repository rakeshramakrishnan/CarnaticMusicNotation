from MIDIread import *
from Note import *
from Raagam import *

RaagamObj = Raagam('Mohanam', 28)
filename = 'raghuvamsa4.mid'
note_list = []
note_list = MIDIToNoteList(filename)

swaram_list = []

for i in note_list:
    notetemp = Note(i, RaagamObj)
    swaram_list.append(notetemp)
    
print swaram_list
