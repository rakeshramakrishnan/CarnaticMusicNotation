import texwrite as t
import entharo_notes_mult_pages as entharo
import os

def conv_dict_note(note=' ', length=None, oct=None, varn=None, verse=None):
    note_dict = {}
    if note != ' ':
        note_dict['note'] = note
    else:
        note_dict['note'] = ' '
    if oct != None:
        note_dict['oct'] = oct
    if varn != None:
        note_dict['varn'] = varn
    if verse != None:
        note_dict['verse'] = verse
    if length !=None:
        note_dict['length'] = length
    
    return note_dict


def create_tabsubspace(count):
    tabsubspace = []
    temp = []
    try:
        temp = note_dict_list[count]
    except IndexError:
        note_dict_list.append(conv_dict_note())
    
    if note_dict_list[count].has_key('length') == True:
        if note_dict_list[count]['length'] == 0.5:
            tabsubspace.append(note_dict_list[count])
            tabsubspace.append(note_dict_list[count + 1])
            count = count + 1;
    else:
        tabsubspace.append(note_dict_list[count])
    count = count + 1
    return (tabsubspace, count)
        
def create_tabspace(f, SwarasPerAksharam, count):
    # Tabspace definition
    tabspace = []
    
    for i in range(0, SwarasPerAksharam):
        tabsubspace = []
        tabsubspace, count = create_tabsubspace(count)
        tabspace.append(tabsubspace)
        
    t.tex_tabspace(f, tabspace)
    f.write(r'\hfill%')
    f.write('\n')
    return count
    
def create_line(f, NumAksharam, SwarasPerAksharam, count, linecount):
    # Line Definition
    f.write(r'\begin{changemargin}{-0.8in}{-0.8in}')
    f.write('\n')
    
    for i in range(0, NumAksharam):
        count = create_tabspace(f, SwarasPerAksharam, count)
    
    # End line 1
    f.write(r'\textbar\textbar \\[5mm]%')
    f.write('\n')
    f.write(r'\end{changemargin}')
    f.write('\n\n')
    linecount = linecount + 1
    return (count, linecount)


# Starting of trial program    
# Parameters
NumAksharam = 4
SwarasPerAksharam = 4
max_lines_page = 12

# Opening file    
f = open('entharotrial.tex','w')

package = ['[paper=a4paper,margin=1.0in]{geometry}', '{amsmath}']

t.tex_preamble(f, package)
t.tex_beginning(f, 'Large')
t.tex_linestretch(f, 1.5)    
    
# t.tex_section(f, 'Trial')

# Getting note list
note_dict_list = []
count = 0
for i in entharo.entharo_note_list:
    note, length, oct, varn, verse = i
    note_dict_list.append(conv_dict_note(note, length, oct, varn, verse))

n = len(note_dict_list)

leftpage = open('leftpage.txt', 'w')
rightpage = open('rightpage.txt','w')

linecount = 1
pagecount = 1

while count < n:
    if linecount <= 2*max_lines_page:
        if linecount %2 == 1:
            count, linecount = create_line(leftpage, NumAksharam, SwarasPerAksharam, count, linecount)
        else:
            count, linecount = create_line(rightpage, NumAksharam, SwarasPerAksharam, count, linecount)
    else:
        # Since linecount has exceeded the maximum number of lines in a page, let us write it to the 
        # main file and reset the linecount flag. Here, the leftpage and rightpage objects are opened
        # in write mode, and we need to close it in order to be able to open in write mode.
        leftpage.close()
        rightpage.close()
        leftpage = open('leftpage.txt')
        rightpage = open('rightpage.txt')
        leftpage_content = leftpage.read()
        rightpage_content = rightpage.read()
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

# Write any remaining data to the file
leftpage.close()
rightpage.close()
leftpage = open('leftpage.txt')
rightpage = open('rightpage.txt')
leftpage_content = leftpage.read()
rightpage_content = rightpage.read()
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
leftpage.close()
rightpage.close()

# count = create_line(f, NumAksharam, SwarasPerAksharam, count)

f.write('\n')

t.tex_end(f)

f.close()
os.remove('leftpage.txt')
os.remove('rightpage.txt')
