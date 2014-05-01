from Raagam import *
from Taalam import *
from Note import *
from Page import *
from InputToSwaram import *
from MIDIread import *
from MIDIwrite import *
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
        
        self.SongName = raw_input('Enter the song name: ')
        
        self.TexFile = open(self.SongName + '.tex', 'w')
        
        self.RaagamName = raw_input('Enter the name of the Raagam: ')
        self.RaagamObj = Raagam(self.RaagamName)
        
        self.TaalamName = raw_input('Enter the name of the Taalam: ')
        self.TaalamObj = Taalam(self.TaalamName)
        
        choice_flag = 1
        while choice_flag == 1:
            print 'You now have two choices: '
            print '1. Enter the notes of the song manually'
            print '2. Specify the filename of the MIDI file to extract notes from it'
            choice = raw_input('Choose 1 or 2: ')
            if choice == '1':
                
                choice_flag = 0
            
            elif choice == '2':
                filename = raw_input('Enter the filename of the MID file with the .mid extension: ')
                # filename = 'raghuvamsa4.mid'
                self.MIDI_note_dict_list = []
                self.MIDI_note_dict_list = MIDIToNoteList(filename)
                self.NoteList = []
                for i in MIDI_note_dict_list:
                    notetemp = Note.MIDIToSwaram(i, self.RaagamObj)
                    self.NoteList.append(notetemp)
                choice_flag = 0
            else:
                print 'Invalid Choice!! Enter again'

        
        print 'Have a great time!!'
        
    
    def NoteInput(self):
        
        NoteMasterList = []
        section_flag = 1
        while section_flag == 1:
            self.Section = raw_input('Enter the section of the song: ')
            print 'Now enter the notes of the song: \n'        
            self.InputNoteList = []
            self.InputNoteList = GetInputNoteDictFromInput()
            self.NoteList = []
            for i in self.InputNoteList:
                notetemp = Note.InputToSwaram(i, self.RaagamObj)
                self.NoteList.append(notetemp)
                self.NoteMasterList.append(notetemp)
            
            self.CreatePages() 
            
            print 'Do you want to enter more notes?'
            while 1:
                inputchoice = raw_input('Enter 1 for yes and 0 for no')
                if inputchoice == '1':
                    section_flag = 1
                    break
                elif inputchoice == '0':
                    section_flag = 0
                    break
                else:
                    print 'Invalid Choice!!'

        
        self.WritePageToFile()
        
        filename = self.SongName + '.mid'
        NoteListToMIDI(filename, self.NoteMasterList, self.TaalamObj.NumberOfAksharam, self.TaalamObj.SwarasPerAksharam)
    
    
    def CreateTitlepage(self):
        
    
    
    def CreatePages(self):
        self.PageList = []
        self.MaxLinesInAPage = 12
        
        
        n = len(self.NoteList)
        while self.count < NoteList:                
            # Creating a Page object
            self.CurrPage = Page(self.MaxLinesInAPage)
            result = self.CurrPage.CreateLines(count)
            if result == 1:
                self.WritePageToFile()
                self.PageList.append(self.CurrPage)
            
        
    def WritePageToFile(self):
        self.CurrPage.leftpage.close()
        self.CurrPage.rightpage.close()
        self.CurrPage.leftpage = open('leftpage.txt')
        self.CurrPage.rightpage = open('rightpage.txt')
        self.CurrPage.leftpage_content = leftpage.read()
        self.CurrPage.rightpage_content = rightpage.read()
        t.tex_centering(f, 'Pallavi')
        f.write(leftpage_content)
        f.write('\n')
        f.write(r'\newpage')
        f.write('\n')
        t.tex_centering(f, ' ')
        f.write(rightpage_content)
        f.write('\n')
        f.write(r'\newpage')
        f.write('\n')
        
        # Close and reopen again
        leftpage.close()
        rightpage.close()
        leftpage = open('leftpage.txt', 'w')
        rightpage = open('rightpage.txt','w')
        
        # Reset linecount
        linecount = 1
    

    
                
                
                
if __name__ == '__main__':
    songbook = SongBook()
    songbook.CreateSongBook()
    
    
    
        
        