import texwrite as t
import entharo_notes as entharo

def conv_dict_note(note, length = None, oct=None, varn=None, verse=None):
    note_dict = {}
    note_dict['note'] = note
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
    
def create_line(f, NumAksharam, SwarasPerAksharam, count):
    # Line Definition
    f.write(r'\begin{changemargin}{-0.8in}{-0.8in}')
    f.write('\n')
    
    for i in range(0, NumAksharam):
        count = create_tabspace(f, SwarasPerAksharam, count)
    
    # End line 1
    f.write(r'\textbar\textbar \\%')
    f.write('\n')
    f.write(r'\end{changemargin}')
    f.write('\n\n')
    return count


# Starting of trial program    
# Parameters
NumAksharam = 4
SwarasPerAksharam = 4

# Opening file    
f = open('entharotrial.tex','w')

package = ['[paper=a4paper,margin=1.0in]{geometry}', '{amsmath}']

t.tex_preamble(f, package)
t.tex_beginning(f, 'large')
t.tex_linestretch(f, 1.5)    
    
t.tex_section(f, 'Trial')
f.write('This is a trial')
f.write(r'\\')
f.write('\n')

# Getting note list
note_dict_list = []
count = 0
for i in entharo.entharo_note_list:
    note, length, oct, varn, verse = i
    note_dict_list.append(conv_dict_note(note, length, oct, varn, verse))

n = len(note_dict_list)
while count < n:
    count = create_line(f, NumAksharam, SwarasPerAksharam, count)

f.write('\n')

t.tex_end(f)
f.close()
