from Raagam import *
from Note import *
import MappingList
import re
# input_swaram, input_swarasthanam_char, input_octave_char, note_length, latex_note_verse, raagam_obj

def GetInputNoteDictFromInput(line = None):

    # with open('NoteMapper.txt', 'r') as f:
        # mapping_list = []
        # for line in f:
            # if line.startswith('#') == False:
                # NoteListTemp = []
                # quoteflag = 0
                # for i in range(0,len(line)):
                    # if quoteflag == 0 and (line[i]== '\'' or line[i] == '\"'):
                        # quoteflag = 1
                        # tempstr = ''
                    # elif quoteflag == 1 and (line[i].isalnum() or line[i] == '/' or line[i] == ','): 
                        # tempstr = tempstr + line[i]
                    # elif quoteflag == 1 and (line[i]== '\'' or line[i] == '\"'):
                        # quoteflag = 0
                        # NoteListTemp.append(tempstr)
                        # tempstr = ''
                # if quoteflag == 1:
                    # quoteflag = 0
                    # NoteListTemp.append(tempstr)
                # mapping_list.append(NoteListTemp)

    mapping_list = []
    mapping_list = MappingList.GetMappingList() 
    
    input_note_list = [] 

    mapping_swaram_list = [i[1] for i in mapping_list]
    mapping_swaram_list = [i[0:-1] if len(i)>1 else i for i in mapping_swaram_list]
    mapping_swaram_list = list(set(mapping_swaram_list))

    mapping_swarasthanam_list = [i[1] for i in mapping_list]
    mapping_swarasthanam_list = [i[-1] for i in mapping_swarasthanam_list if len(i)>1]
    mapping_swarasthanam_list = list(set(mapping_swarasthanam_list))
    
    note_flag = 0
    note_length = 0
    note_verse_flag = 0
    latex_note_verse = ''
    # note_flag = 0
    fast_multiplier = 1
    input_swaram_dict = {}

    if line == None:

        input_flag = 1

        print 'Enter the notes for the song. Enter \'0\' to stop entering notes'
        
        while input_flag:
            input_str = raw_input('\>: ')
            
            if input_str == '0':
                input_flag = 0
                input_swaram_dict['length'] = note_length
                input_swaram_dict['verse'] = latex_note_verse
                input_note_list.append(input_swaram_dict)
                break
            
            tempstr = ''
            for i in mapping_swaram_list:
                tempstr = tempstr + '(' + i + ')' + '|'   
            tempstr = tempstr + '(.)' + '|' + '(\')' + '(()' + '())'    
            input_str = re.split(tempstr, input_str)
            input_str = [i for i in input_str if i !=None and i != '' and i != ' ']
            
            for i in input_str:
                if i == '{':
                        fast_multiplier = 0.5
                elif i == '}':
                        fast_multiplier = 1
                elif note_flag == 0:
                    if i in mapping_swaram_list and note_verse_flag == 0:
                        note_flag = 1
                        input_swaram_dict['swaram'] = i
                        input_swaram_dict['octave'] = 0
                        input_swaram_dict['verse'] = latex_note_verse
                        input_swaram_dict['fast'] = fast_multiplier
                        note_length = note_length + fast_multiplier*1
                elif note_flag == 1:
                    if i in mapping_swaram_list and note_verse_flag == 0:
                        input_swaram_dict['length'] = note_length
                        input_swaram_dict['verse'] = latex_note_verse
                        latex_note_verse = ''
                        input_note_list.append(input_swaram_dict)
                        note_length = 0
                        input_swaram_dict = {}
                        input_swaram_dict['swaram'] = i
                        input_swaram_dict['fast'] = fast_multiplier
                        input_swaram_dict['octave'] = 0
                        note_length = note_length + fast_multiplier*1
                    elif i in mapping_swarasthanam_list:
                        input_swaram_dict['swarasthanam'] = i
                    elif i == ',':
                        note_length = note_length + fast_multiplier*1
                    elif i == '.':
                        input_swaram_dict['octave'] = -1
                        input_swaram_dict['octavechar'] = i
                    elif i == '\'':
                        input_swaram_dict['octave'] = 1
                        input_swaram_dict['octavechar'] = i
                    elif i == '(':
                        note_verse_flag = 1
                    elif i == ')':
                        note_verse_flag = 0
                    elif note_verse_flag == 1 and i !='(':
                        latex_note_verse = latex_note_verse + i
        
    else:
        tempstr = ''
        for i in mapping_swaram_list:
            tempstr = tempstr + '(' + i + ')' + '|'   
        tempstr = tempstr + '(.)' + '|' + '(\')' + '(()' + '())'    
        line = re.split(tempstr, line)
        line = [i for i in line if i !=None and i != '' and i != ' ']
        
        for i in line:
            if i == '{':
                    fast_multiplier = 0.5
            elif i == '}':
                    fast_multiplier = 1
            elif note_flag == 0:
                if i in mapping_swaram_list and note_verse_flag == 0:
                    note_flag = 1
                    input_swaram_dict['swaram'] = i
                    input_swaram_dict['octave'] = 0
                    input_swaram_dict['verse'] = latex_note_verse
                    input_swaram_dict['fast'] = fast_multiplier
                    note_length = note_length + fast_multiplier*1
            elif note_flag == 1:
                if i in mapping_swaram_list and note_verse_flag == 0:
                    input_swaram_dict['length'] = note_length
                    input_swaram_dict['verse'] = latex_note_verse
                    latex_note_verse = ''
                    input_note_list.append(input_swaram_dict)
                    note_length = 0
                    input_swaram_dict = {}
                    input_swaram_dict['swaram'] = i
                    input_swaram_dict['fast'] = fast_multiplier
                    input_swaram_dict['octave'] = 0
                    note_length = note_length + fast_multiplier*1
                elif i in mapping_swarasthanam_list:
                    input_swaram_dict['swarasthanam'] = i
                elif i == ',':
                    note_length = note_length + fast_multiplier*1
                elif i == '.':
                    input_swaram_dict['octave'] = -1
                    input_swaram_dict['octavechar'] = i
                elif i == '\'':
                    input_swaram_dict['octave'] = 1
                    input_swaram_dict['octavechar'] = i
                elif i == '(':
                    note_verse_flag = 1
                elif i == ')':
                    note_verse_flag = 0
                elif note_verse_flag == 1 and i !='(':
                    latex_note_verse = latex_note_verse + i
        
        # Writing remaining data
        input_swaram_dict['length'] = note_length
        input_swaram_dict['verse'] = latex_note_verse
        input_note_list.append(input_swaram_dict)    
        
        
    return input_note_list


if __name__ == '__main__':
    raagamObj = Raagam('Mohanam', 28)
    input_note_list = GetInputNoteDictFromInput()

    note_list = []
    for i in input_note_list:
        notetemp = Note.InputToSwaram(i, raagamObj)
        note_list.append(notetemp)


