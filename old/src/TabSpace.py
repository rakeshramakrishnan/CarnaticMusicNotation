from Note import *
from TabSubSpace import *

class TabSpace(object):
    def __init__(self, tab_space_width = 0.23, swaras_per_aksharam = None):
        self.LatexFastFunctionDefinition = r'\newcommand{\tolstrut}{%' + '\n' + \
                                           r'\vrule height\dimexpr\fontcharht\font`\A+0.9ex\relax width 0pt\relax}' + '\n\n' + \
                                           r'\DeclareRobustCommand{\fast}[1]{%' + '\n' + \
                                           r'\ensuremath{\overline{\mbox{\tolstrut#1}}}}' + '\n\n'
        self.LatexFastFunctionStarting= r'\fast{%'
        self.LatexFastFunctionEnding = r'}%'
        self.TabSpaceWidth = tab_space_width
        self.NumberOfTabSubSpaces = swaras_per_aksharam
        self.TabSubSpaceList = []
    
    
    def AddTabSubSpacesToTabSpace(self, file_handle, tab_sub_space_list, tab_sub_space_list_count):
        
        notes_ending_flag = self.NumberOfTabSubSpaces
        tab_sub_space_list_count_starting = tab_sub_space_list_count
        
        for i in range(self.NumberOfTabSubSpaces):
            try:
                temp = tab_sub_space_list[tab_sub_space_list_count_starting + i]
            except IndexError:
                notes_ending_flag = i
                break
        
        curr_fast_flag = 0
        
                
        file_handle.write(r'\begin{minipage}[t][][s]{' + str(self.TabSpaceWidth) + r'\linewidth}')
        file_handle.write('\n\t')
        file_handle.write(r'\centering%')
        file_handle.write('\n\t')
        
        for i in range(notes_ending_flag):
            
            
            if curr_fast_flag == 0 and tab_sub_space_list[tab_sub_space_list_count].GetFastFlag() == 1:
                curr_fast_flag = 1
                file_handle.write(self.LatexFastFunctionStarting)
                file_handle.write('\n\t')
            
            elif curr_fast_flag == 1 and tab_sub_space_list[tab_sub_space_list_count].GetFastFlag() == 1:
                pass
            
            elif curr_fast_flag == 1 and tab_sub_space_list[tab_sub_space_list_count].GetFastFlag() == 0:
                curr_fast_flag = 0
                file_handle.write(self.LatexFastFunctionEnding)
                file_handle.write('\n\t')
                
            elif curr_fast_flag == 0 and tab_sub_space_list[tab_sub_space_list_count].GetFastFlag() == 0:
                curr_fast_flag = 0  

               
            #####
            # Writing the Tab Sub Space Note
            file_handle.write(tab_sub_space_list[tab_sub_space_list_count].LatexNote)
            self.TabSubSpaceList.append(tab_sub_space_list[tab_sub_space_list_count].LatexNote)
            #####                
            file_handle.write('\n\t')
            tab_sub_space_list_count = tab_sub_space_list_count + 1
        
        if curr_fast_flag == 1:
                curr_fast_flag = 0
                file_handle.write(self.LatexFastFunctionEnding)
                file_handle.write('\n\t')
                    
        if notes_ending_flag != 0:
            file_handle.write(r'\\%')
            file_handle.write('\n\t')
        
        
        # Writing the verses
        for i in range(notes_ending_flag):
            #####
            # Writing the Tab Sub Space Verse
            file_handle.write(tab_sub_space_list[tab_sub_space_list_count_starting + i].LatexVerse)
            self.TabSubSpaceList.append(tab_sub_space_list[tab_sub_space_list_count_starting + i].LatexVerse)
            #####                
            file_handle.write('\n\t')
            
        if notes_ending_flag != 0:
            file_handle.write(r'\\%')
            file_handle.write('\n\t')
        
        # Exiting the TabS pace
        file_handle.write(r'\end{minipage}%')
                
        if notes_ending_flag != self.NumberOfTabSubSpaces:
            return -1
        else:
            return tab_sub_space_list_count
 
        
            
        
      
        
