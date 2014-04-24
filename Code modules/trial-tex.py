import texwrite as t

def conv_dict_note(note, oct=None, varn=None, verse=None):
    note_dict = {}
    note_dict['note'] = note
    if oct != None:
        note_dict['oct'] = oct
    if varn != None:
        note_dict['varn'] = varn
    if verse != None:
        note_dict['verse'] = verse
    
    # if oct == none:
        # if varn == none:
            # note_dict = {'note':note}
        # else:
            # note_dict = {'note':note, 'varn':varn}
    # else:
        # if varn == none:
            # note_dict = {'note':note}
        # else:
            # note_dict = {'note':note, 'oct':oct, 'varn':varn}
        
    return note_dict

f = open('textrial.tex','w')

package = ['[paper=a4paper,margin=1.0in]{geometry}', '{amsmath}']

t.tex_preamble(f, package)
t.tex_beginning(f, 'large')
t.tex_linestretch(f, 1.5)
t.tex_section(f, 'Trial')
f.write('This is a trial')
f.write(r'\\')
f.write('\n')

# Line 1
f.write(r'\begin{changemargin}{-0.8in}{-0.8in}')
f.write('\n\n')

tabsubspace = []
tabspace = []
# Tabspace 1
tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

t.tex_tabspace(f, tabspace)
tabspace = []
f.write(r'\hfill%')
f.write('\n')

# Tabspace 2
tabsubspace.append(conv_dict_note('S', None, None, 'En'))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note('R', None, None, 'Tha'))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

t.tex_tabspace(f, tabspace)
tabspace = []
f.write(r'\hfill%')
f.write('\n')

# Tabspace 3
tabsubspace.append(conv_dict_note('R', None, None, 'Ro'))
tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note('G', None, None, None))
tabsubspace.append(conv_dict_note('R', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note('S', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

t.tex_tabspace(f, tabspace)
tabspace = []
f.write(r'\hfill%')
f.write('\n')

# Tabspace 4
tabsubspace.append(conv_dict_note('N', -1, None, 'Ma'))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note('S', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note('R', None, None, None))
tabsubspace.append(conv_dict_note(',', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

tabsubspace.append(conv_dict_note('G', None, None, None))
tabsubspace.append(conv_dict_note('R', None, None, None))
tabspace.append(tabsubspace)
tabsubspace = []

t.tex_tabspace(f, tabspace)
tabspace = []
f.write(r'\hfill%')
f.write('\n')

# End line 1
f.write(r'\textbar\textbar \\%')
f.write('\n')
f.write(r'\end{changemargin}')
f.write('\n')

f.write('\n')

t.tex_end(f)
f.close()
