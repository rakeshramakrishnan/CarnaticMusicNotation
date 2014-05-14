from Raagam import *
from Taalam import *
from Note import *
from Page import *
from TabSpace import *
from TabSubSpace import *
import midi
import copy
import os
import shutil


from InputToSwaram import *
from MIDIread import *
from MIDIwrite import *
import MappingList


from TexTitlePagePreamble import *
import texwrite as t
import re

class SongBook(object):
    def __init__(self):
        print '\n\n'
        print 'Welcome to new SongBook creation!!!'
        print 'Use NoteMapper.txt to define your conventions:'
        print 'You need to know data about Raagam of song in order to proceed'
        print 'Ensure that RaagamDB.txt contains some Raagams. If not, don\'t worry, '
        print 'Ensure that you know about the Raagam - you can enter it in-situ'
        print '\n\n'
        
        self.SongName = raw_input('Enter the song name: ')
            
        self.RaagamName = raw_input('Enter the name of the Raagam: ')
        self.RaagamObj = Raagam(self.RaagamName)
        
        print '\n\n'
        
        self.TaalamName = raw_input('Enter the name of the Taalam: ')
        self.TaalamObj = Taalam(self.TaalamName)
        
        print '\n\n'
    
    
    def CreateSongBook(self):
        self.TabSubSpaceList = []
        self.SectionAndTabSubSpaceList = []
        choice_flag = 1
        while choice_flag == 1:
            print 'You now have two choices: '
            print '1. Enter the notes of the song manually'
            print '2. Specify the filename of the MIDI file to extract notes from it'
            print '3. Enter the filename of the text file which contains the input notes'
            choice = raw_input('Choose 1 or 2 or 3: ')
            print '\n\n'
            if choice == '1':
                # Enter the notes 
                self.NoteInput()
                
                # Create the Song Latex File
                # self.CreateSongLatexFile()
                
                print 'Writing to MIDI'
                # Create the MIDI file
                filename = self.SongName + '.mid'
                NoteListToMIDI(filename, self.NoteMasterList, self.TaalamObj.NumberOfAksharam, self.TaalamObj.SwarasPerAksharam)
                choice_flag = 0
            
            elif choice == '2':
                filename = raw_input('Enter the filename of the MID file with the .mid extension: ')
                print '\n\n'
                # filename = 'raghuvamsa4.mid'
                self.MIDI_note_dict_list = []
                self.MIDI_note_dict_list = MIDIToNoteList(filename)
                self.NoteList = []
                for i in self.MIDI_note_dict_list:
                    notetemp = Note.MIDIToSwaram(i, self.RaagamObj)
                    self.NoteList.append(notetemp)
                
                self.CurrSectionName = 'Main Song'
                self.AddToTabSubSpaceList()
                self.AddToSectionWiseTabSubSpaceList()
                
                # Create the Song Latex File
                # self.CreateSongLatexFile()
                choice_flag = 0
            
            elif choice == '3':
                filename = raw_input('Enter the filename of the text file with the .txt extension: ')
                print '\n\n'
                self.NoteMasterList = []
                start_flag = 0
                with open(filename, 'r') as f:
                    for line in f:
                        if line.startswith('"') == True:
                            if start_flag == 1:
                                self.AddToSectionWiseTabSubSpaceList()
                            self.CurrSectionName = line[1:-2]
                            # If the next section name is read, write the current section
                                                            
                        elif line.startswith(' ') == True or line.startswith('\n') == True:
                            pass
                        else:
                            if start_flag == 0:
                                start_flag = 1
                            self.InputNoteList = []
                            self.InputNoteList = GetInputNoteDictFromInput(line)
                            self.NoteList = []
                            for i in self.InputNoteList:
                                notetemp = Note.InputToSwaram(i, self.RaagamObj)
                                self.NoteList.append(notetemp)
                                notetemp2 = copy.deepcopy(notetemp)
                                self.NoteMasterList.append(notetemp2)
                            ###################################################################################
                            # Write the current notes to TabSubSpace List
                            self.AddToTabSubSpaceList()
                
                # Writing the last section to section-wise tab subspace list
                self.AddToSectionWiseTabSubSpaceList()
                choice_flag = 0
                
                # Writing to MIDI
                print 'Writing to MIDI\n\n'
                
                # Create the MIDI file
                filename = self.SongName + '.mid'
                NoteListToMIDI(filename, self.NoteMasterList, self.TaalamObj.NumberOfAksharam, self.TaalamObj.SwarasPerAksharam)
                        
            else:
                print 'Invalid Choice!! Enter again'

        
        print 'Notes Translated!!'
        
    
    def NoteInput(self):
        
        self.NoteMasterList = []
        
        input_flag = 1 
        section_flag = 1
        
        while input_flag == 1:
            print '\n\n'
            self.CurrSectionName = raw_input('Enter the name of the section of the song: ')
            while section_flag == 1:
                print '\n\n'
                print 'Now enter the notes of the song: \n'        
                self.InputNoteList = []
                self.InputNoteList = GetInputNoteDictFromInput()
                self.NoteList = []
                for i in self.InputNoteList:
                    notetemp = Note.InputToSwaram(i, self.RaagamObj)
                    self.NoteList.append(notetemp)
                    notetemp2 = copy.deepcopy(notetemp)
                    self.NoteMasterList.append(notetemp2)
                
                ###################################################################################
                # Write the current notes to TabSubSpace List
                self.AddToTabSubSpaceList()
                ###################################################################################
                
                flag = 1
                
                while flag == 1:
                    print '\n\n'
                    section_choice = raw_input('Enter notes for the same section? (Y or N): ')
                    if section_choice.upper() == 'N':
                        section_flag = 0 
                        flag = 0
                        break
                    elif section_choice.upper() == 'Y':
                        section_flag = 1
                        flag = 0
                        break
                    else:
                        print 'Invalid Choice!!'
            
            # Add to Section Wise Tab sub space list
            self.AddToSectionWiseTabSubSpaceList()
            
            flag = 1
            while flag == 1:
                print '\n\n'
                input_choice = raw_input('Do you want to enter more notes at all? (Y or N): ')
                if input_choice.upper() == 'Y':
                    input_flag = 1
                    section_flag = 1
                    flag = 0
                    break
                elif input_choice.upper() == 'N':
                    input_flag = 0
                    flag = 0
                    break
                else:
                    print 'Invalid Choice!!'

    
    def AddToTabSubSpaceList(self):
        
        n = len(self.NoteList)
        count = 0
        curr_length = 0
        tbsspace_length = 0
        tempnotestr = ''
        tempversestr = ''
                
        while count < n:
            if self.NoteList[count].GetNoteFastFlag() == 1:
                curr_length = self.NoteList[count].GetNoteLength()
                
                tempnotestr = tempnotestr + self.NoteList[count].GetLatexNote()
                tempversestr = tempversestr + self.NoteList[count].GetLatexVerse()
                self.NoteList[count].SetLatexNote(',')
                self.NoteList[count].SetNoteLength(curr_length - 0.5)
                tbsspace_length = tbsspace_length + 0.5
                
                # To write to tabsubspace list
                if tbsspace_length == 1:
                    t = TabSubSpace(tempnotestr, tempversestr, 1)
                    self.TabSubSpaceList.append(t)
                    tempnotestr = ''
                    tempversestr = ''
                    tbsspace_length = 0
            
            else:
                curr_length = self.NoteList[count].GetNoteLength()
                t = TabSubSpace(self.NoteList[count].GetLatexNote(), self.NoteList[count].GetLatexVerse(), 0)
                self.TabSubSpaceList.append(t)
                self.NoteList[count].SetLatexNote(',')
                self.NoteList[count].SetNoteLength(curr_length - 1)
            
            # To check and read next note
            if self.NoteList[count].GetNoteLength() == 0:
                count = count + 1
        
        
    def AddToSectionWiseTabSubSpaceList(self):
        section_and_tab_space = []
        section_and_tab_space.append(self.CurrSectionName)
        section_and_tab_space.append(self.TabSubSpaceList)
        
        self.SectionAndTabSubSpaceList.append(section_and_tab_space)
        
        self.TabSubSpaceList = []
        
            
    def InitiateBookCreationSequence(self):
        
        self.TexFile = open(self.SongName + '.tex', 'w')
        
        package = ['[paper=a4paper,margin=1.0in]{geometry}', '{amsmath}', '[svgnames]{xcolor}', '{fancyhdr}', '{tikz}']
        
        t.tex_preamble(self.TexFile, package)
        PutTitlePreamble(self.TexFile, self.SongName, self.RaagamName, self.TaalamName, self.RaagamObj.ArohanamTex, self.RaagamObj.AvarohanamTex)
        
        t.tex_beginning(self.TexFile, 'Large')
        
        self.TexFile.write(r'\begin{titlepage}' + '\n')
        self.TexFile.write(r'% The line below puts the curly braces and the title' + '\n')
        self.TexFile.write(r'\titleBC %' + '\n')
        self.TexFile.write(r'\titlepagedecoration' + '\n')
        self.TexFile.write(r'\end{titlepage}' + '\n')
        
        t.tex_linestretch(self.TexFile, 1.5)    
        
        #############################################
        
        self.CreatePages()
        
        #############################################
        self.TexFile.write('\n\n')
        self.TexFile.write(r'\end{document}')
        self.TexFile.close()
        
        os.remove('leftpage.txt')
        os.remove('rightpage.txt')
        
        if os.path.isdir(self.SongName) == True:
            shutil.rmtree(self.SongName)
            
        os.mkdir(self.SongName)
        texfilestr = self.SongName + r'/' + self.SongName + r'.tex'
        midfilestr = self.SongName + r'/' + self.SongName + r'.mid'
        shutil.move(self.SongName + r'.tex', texfilestr)
        shutil.move(self.SongName + r'.mid', midfilestr)
       
    
    def CreatePages(self):
        self.PageList = []
        self.MaxLinesInAPage = 12
        
        self.CurrPage = Page(self.MaxLinesInAPage)
        num_sections = len(self.SectionAndTabSubSpaceList)
        
        result = 0
        
        section_and_tab_sub_space_list_index = 0
        
        while section_and_tab_sub_space_list_index < num_sections:
            self.CurrPage.PutSectionTitle(self.SectionAndTabSubSpaceList[section_and_tab_sub_space_list_index][0])
            while result != -1:
                result, linecount = self.CurrPage.CreatePage(self.TaalamObj.NumberOfAksharam, self.TaalamObj.SwarasPerAksharam, \
                                                            self.TaalamObj.TabSpaceWidth, \
                                              self.SectionAndTabSubSpaceList[section_and_tab_sub_space_list_index][1], result)
                if result == -1:
                    pass
                elif linecount >= self.MaxLinesInAPage*2:
                    self.PageList.append(self.CurrPage)
                    ########################################################
                    self.WritePageToFile()
                    ########################################################
                    self.CurrPage = Page(self.MaxLinesInAPage)
            
            section_and_tab_sub_space_list_index = section_and_tab_sub_space_list_index + 1
            result = 0
        
        
        ############################################################
        # Write out the remaining data to the Tex file
        self.WritePageToFile()
        #############################################################
                
        
    def WritePageToFile(self):
        self.CurrPage.LeftPage.close()
        self.CurrPage.RightPage.close()
        self.CurrPage.LeftPage = open('leftpage.txt')
        self.CurrPage.RightPage = open('rightpage.txt')
        self.CurrPage.leftpage_content = self.CurrPage.LeftPage.read()
        self.CurrPage.rightpage_content = self.CurrPage.RightPage.read()
        self.TexFile.write(self.CurrPage.leftpage_content)
        self.TexFile.write('\n')
        self.TexFile.write(r'\newpage')
        self.TexFile.write('\n')
        self.TexFile.write(self.CurrPage.rightpage_content)
        self.TexFile.write('\n')
        self.TexFile.write(r'\newpage')
        self.TexFile.write('\n')
        
        # Close and reopen again
        self.CurrPage.LeftPage.close()
        self.CurrPage.RightPage.close()
        
        # Reset linecount
        linecount = 1
    

    
###############################################################################################################                
                
                
if __name__ == '__main__':
    songbook = SongBook()
    
    notes_satisfaction_flag = 0
    
    while notes_satisfaction_flag == 0:
        songbook.CreateSongBook()
        print '\n\n'
        print 'You have now entered the notes of the song. \n'
        choice = raw_input('Shall we generate the Latex Code of the song book? (Y or N): ')
        if choice.upper() == 'Y':
            songbook.InitiateBookCreationSequence()
        
        input_wrong_flag = 1
        while input_wrong_flag == 1:
            choice = raw_input('Enter the notes again? (Y or N): ')
            if choice.upper() == 'Y':
                notes_satisfaction_flag = 0
                input_wrong_flag = 0
            elif choice.upper() == 'N':
                notes_satisfaction_flag = 1
                input_wrong_flag = 0
            else: 
                print 'Invalid Choice'
                input_wrong_flag = 1
    
    
    
        
        