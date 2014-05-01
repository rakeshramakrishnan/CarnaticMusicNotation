from Raagam import *
from Taalam import *
from Note import *
from InputToSwaram import *
from MIDIread import *
from MIDIwrite import *
from Line import *
import MappingList
import texwrite as t

class Page(object):
    def __init__(self, max_lines_in_a_page = 12):
        self.MaxLinesInPage = max_lines_in_a_page
        self.LeftPage = open('leftpage.txt', 'w')
        self.RightPage = open('rightpage.txt','w')
        
        
    def CreateLine(self, page_file_handle, num_aksharam, swaras_per_aksharam, count, linecount, note_duration_carryover):
        for i in self.MaxLinesOfPage:
            
        
    