from __future__ import division
import midi

# In this script, we explore the possibilities of reading note data from a MIDI file. 
# The following features are made
#    1. Removes noise in MIDI file by rounding off while calculating duration
#    2. Assumes simultaneous input (2 notes at same time) to be treated as per 
#       portamento rules (old note cut off when new note is encountered)
#    3. Following from the above case, the "R,GR" mode of playing (where there is 
#       a single R for all times and G is pressed in between) gives the result
#       as "R, G R"
#
# Output is a note_list which is a list of 'note' dictionaries. The 'note' dictionary
# contains the note value and it's duration, where least count = 0.5. The tempo information
# from the MIDI file and the 'tick' unit is used to get the 'duration' as required. 
# If required, the value of duration can be scaled up or down by factors of 2

pattern = midi.read_midifile("raghuvamsa4.mid")
count = 0;
note = {}
note_list = []

tick_tempo = pattern[0][1].data[2]

curr_note = 0
curr_note_duration = 0

for j in range(1,len(pattern[1]) - 1):
    if type(pattern[1][j]) == midi.events.NoteOnEvent:
        curr_note_duration = curr_note_duration + pattern[1][j].tick
        if (round(curr_note_duration * 2.0 / tick_tempo)/2):
            note_list.append({'note': curr_note, 'duration':round(curr_note_duration * 2.0 / tick_tempo)/2})
            curr_note_duration = 0
        curr_note = pattern[1][j].data[0]
    
    elif type(pattern[1][j]) == midi.events.NoteOffEvent:
        curr_note_duration = curr_note_duration + pattern[1][j].tick
        if curr_note == pattern[1][j].data[0]:
            note_list.append({'note': curr_note, 'duration':round(curr_note_duration * 2.0 / tick_tempo)/2})
            curr_note_duration = 0
            curr_note = 0
        elif curr_note == 0:
            note_list.append({'note': pattern[1][j].data[0], 'duration':round(pattern[1][j].tick * 2.0 / tick_tempo)/2})
            curr_note_duration = 0
        
# print note_list    

duration_net = 0

for i in note_list:
    duration_net = duration_net + i['duration']

print 'Net Duration = ', duration_net