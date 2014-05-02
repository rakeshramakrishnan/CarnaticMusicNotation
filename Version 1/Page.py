from Raagam import *
from Taalam import *
from Note import *
from InputToSwaram import *
from MIDIread import *
from MIDIwrite import *
from TabSpace import *
from TabSubSpace import *

import MappingList
import texwrite as t


class Page(object):
    def __init__(self, max_lines_in_a_page = 12):
        self.MaxLinesInPage = 2*max_lines_in_a_page
        self.LeftPage = open('leftpage.txt', 'w')
        self.RightPage = open('rightpage.txt','w')
        self.LineCount = 1
        self.TabSpaceCount = 0
        self.TabSpaceObjectsList = []
        
    def CreatePage(self, num_aksharam, swaras_per_aksharam, tab_space_width, tab_sub_space_list, tab_sub_space_list_count):
            
        self.LineList = []
        
        while self.LineCount <= self.MaxLinesInPage:
            
            # Writing the left page
            tab_sub_space_list_count = self.CreateLine(self.LeftPage, num_aksharam, swaras_per_aksharam, tab_space_width, \
                                                   tab_sub_space_list, tab_sub_space_list_count)
            
            if tab_sub_space_list_count == -1:
                # self.LineCount = 1000
                break
            
            self.LineCount = self.LineCount + 1
            
            # Writing to rightpage
            tab_sub_space_list_count = self.CreateLine(self.RightPage, num_aksharam, swaras_per_aksharam, tab_space_width, \
                                                   tab_sub_space_list, tab_sub_space_list_count)
            
            if tab_sub_space_list_count == -1:
                # self.LineCount = 1000
                break
            
            self.LineCount = self.LineCount + 1
            
        self.LeftPage.write('\n')
        self.RightPage.write('\n')
        
        return (tab_sub_space_list_count, self.LineCount)
        

    def CreateLine(self, file_handle, num_aksharam, swaras_per_aksharam, tab_space_width, tab_sub_space_list, tab_sub_space_list_count):
        
        self.MaxNumTabSpaces = num_aksharam
        self.TabSpacesList = []
        curr_tab_space_num = 1
        
        # line_creation_result = 0
       
        file_handle.write(r'\begin{changemargin}{-0.8in}{-0.8in}')
        file_handle.write('\n')
        
        while curr_tab_space_num <= self.MaxNumTabSpaces:
            tab_space_obj = TabSpace(tab_space_width, swaras_per_aksharam)
            tab_sub_space_list_count = tab_space_obj.AddTabSubSpacesToTabSpace(file_handle, tab_sub_space_list, tab_sub_space_list_count)
            self.TabSpacesList.append(tab_space_obj)
            
            if tab_sub_space_list_count == -1:
                curr_tab_space_num = 10000 # A large value
            
            curr_tab_space_num = curr_tab_space_num + 1
            
            file_handle.write('\n')
            file_handle.write(r'\hfill%')
            file_handle.write('\n')
        
        
        if file_handle == self.LeftPage:
            file_handle.write(r'\textbar \\[5mm]%')
            file_handle.write('\n')
        elif file_handle == self.RightPage:
            file_handle.write(r'\textbar\textbar \\[5mm]%')
            file_handle.write('\n')
        
        
        file_handle.write(r'\end{changemargin}')
        file_handle.write('\n')
        
        # self.LineCount = self.LineCount + 1 
        
        return tab_sub_space_list_count
            
        
    def PutSectionTitle(self, section_name):
        
        self.LeftPage.write(r'\vspace{15pt}')
        self.LeftPage.write('\n\n')
        self.LeftPage.write(r'\section*{\centering\textcolor{blue}{' + section_name + r'}}')
        self.LeftPage.write('\n\n')
        self.RightPage.write(r'\vspace{15pt}')
        self.RightPage.write('\n\n')
        self.RightPage.write(r'\section*{\centering\textcolor{blue}{' + '   ' + r'}}')
        self.LineCount = self.LineCount + 2
        self.RightPage.write('\n\n')
        return self.LineCount
        
        
    