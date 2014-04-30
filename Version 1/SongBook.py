from Raagam import *
from Taalam import *
from Note import *
from InputToSwaram import *
from MIDIread import *
import MappingList



import texwrite as t
import re

class SongBook(object):
    def __init__(self):
        pass
    
    
    def CreateSongBook(self):
        # cls
        print 'Welcome to new SongBook creation!!!'
        print 'Use NoteMapper.txt to define your conventions:'
        print 'You need to know data about Raagam of song in order to proceed'
        print 'Ensure that RaagamDB.txt contains some Raagams. If not, don\'t worry, '
        print 'ensure that you know about the Raagam - you can enter it in-situ'
        
        raagamname = raw_input('Enter the name of tha Raagam: ')
        raagamObj = Raagam(raagamname)
        
        taalamname = raw_input('Enter the name of the Taalam: ')
        taalamObj = Taalam(taalamname)
        
        choice_flag = 1
        while choice_flag == 1:
            print 'You now have two choices: '
            print '1. Enter the notes of the song manually'
            print '2. Specify the filename of the MIDI file to extract notes from it'
            choice = raw_input('Choose 1 or 2: ')
            if choice == '1':
                input_note_list = []
                input_note_list = GetInputNoteDictFromInput()
                note_list = []
                for i in input_note_list:
                    notetemp = Note.InputToSwaram(i, raagamObj)
                    note_list.append(notetemp)
                choice_flag = 0
            
            elif choice == '2':
                filename = raw_input('Enter the filename of the MID file with the .mid extension: ')
                # filename = 'raghuvamsa4.mid'
                MIDI_note_dict_list = []
                MIDI_note_dict_list = MIDIToNoteList(filename)
                note_list = []
                for i in MIDI_note_dict_list:
                    notetemp = Note.MIDIToSwaram(i, raagamObj)
                    note_list.append(notetemp)
                choice_flag = 0
            else:
                print 'Invalid Choice!! Enter again'

        
        for i in note_list:
            print i.__dict__
        
        print 'Have a great time!!'
                
                
                
                
if __name__ == '__main__':
    songbook = SongBook()
    songbook.CreateSongBook()
    
    
    
        
        