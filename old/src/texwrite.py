''' This code is a sample python code to see if I can write data into a 
    tex file. I will write whatever I have written in the boxtrial.tex file. '''

def tex_preamble(f, package):
    # Write out document preamble

    f.write(r'\documentclass[a4paper]{article}')
    f.write('\n\n')
    for i in package:
        f.write(r'\usepackage' + i)
        f.write('\n')
    f.write('\n')
    f.write(r'\setlength\parindent{0pt}')
    f.write('\n\n')
        
    # Changemargin environment definition
    f.write(r'\def\changemargin#1#2{\list{}{\rightmargin#2\leftmargin#1}\item[]}')
    f.write('\n')
    f.write(r'\let\endchangemargin=\endlist')
    f.write('\n\n')
    
    # Tolstrut newcommand definition
    f.write(r'\newcommand{\tolstrut}{%')
    f.write('\n')
    f.write(r'\vrule height\dimexpr\fontcharht\font`\A+0.9ex\relax width 0pt\relax}')
    f.write('\n\n')
    
    # Fast newcommand definition
    f.write(r'\DeclareRobustCommand{\fast}[1]{%')
    f.write('\n')
    f.write(r'\ensuremath{\overline{\mbox{\tolstrut#1}}}}')
    f.write('\n\n')
    
    # Tab Sub Space newcommand definition
    f.write(r'\newcommand{\TBSSpace}[1]{\makebox[0.20\linewidth][c]{$\text{#1}$}}')
    f.write('\n\n')
    
    # Higher octave newcommand definition
    f.write(r'\newcommand{\HOct}[1]{\.{#1}}')
    f.write('\n\n')
    
    # Lower octave newcommand definition
    f.write(r'\newcommand{\LOct}[1]{\d{#1}}')
    f.write('\n\n')

    # Note variation newcommand definition
    f.write(r'\newcommand{\varnote}[1]{$_{\text{#1}}$}')
    f.write('\n\n')
 
def tex_beginning(f, fontsize = 'large'):
    f.write(r'\begin{document}')
    f.write('\n')
    
    # Set font size
    f.write('\\' + fontsize)
    f.write('\n\n')
    # f.write(r'\renewcommand{\baselinestretch}{1.5}')
    # f.write('\n\n')
 
def tex_end(f):
    f.write(r'\end{document}')
    f.write('\n\n')
 
def tex_linestretch(f, linestretch):
    f.write(r'\renewcommand{\baselinestretch}{' + str(linestretch) + r'}')
    f.write('\n\n')
 
def tex_section(f, section):
    f.write(r'\section{' + section + r'}')
    f.write('\n\n')
 
def tex_subsection(f, subsection):
    f.write(r'\subsection{' + subsection + r'}')
    f.write('\n\n')

def tex_centering(f, center_string):
    f.write(r'\begin{center}')
    f.write('\n')
    f.write(r'\textbf{' + center_string + r'} \\[5mm]')
    f.write('\n')
    f.write(r'\end{center}')
    f.write('\n\n')

def tex_vspace(f, vspace):
    f.write(r'\vspace{' + str(vspace) + '}')
    f.write('\n\n')
 
def tex_Tabsubspace(f, tbsspace):
    f.write(r'\TBSspace{')
    for i in tbsspace:
        if i.has_key('oct'):
            if i['oct'] == -1:
                f.write(r'\Loct{' + str(i['note']) + r'}')
            elif i['oct'] == 1:
                f.write(r'\Hoct{' + str(i['note']) + r'}')
            elif i['oct'] == 0:
                f.write(i['note'])
        else:
            f.write(i['note'])
        
        if i.has_key('varn') == True:
            f.write(r'\varnote{' + str(i['varn']) + r'}')
    f.write(r'}%')
    f.write('\n\t')

def tex_Tabsubspaceverse(f, tbsspace):
    f.write(r'\TBSspace{$\boldsymbol{')
    for i in tbsspace:
        if i.has_key('verse'):
            f.write(str(i['verse']))
    f.write(r'}$}%')
    f.write('\n\t')

            

def tex_tabspace(f, tabspace, linewidth = 0.23):
    f.write(r'\begin{minipage}[t][][s]{' + str(linewidth) + r'\linewidth}')
    f.write('\n\t')
    f.write(r'\centering%')
    f.write('\n\t')
    fast_flag = 0
    for i in tabspace:
        if len(i) == 2 and fast_flag == 0:
            fast_flag = 1
            f.write(r'\fast{%')
            f.write('\n\t')
        
        if len(i) != 2 and fast_flag == 1:
            fast_flag = 0
            f.write(r'}%')
            f.write('\n\t')
 
        tex_Tabsubspace(f, i)
    
    if fast_flag==1:
        fast_flag = 0
        f.write(r'}%')
        f.write('\n\t')
    f.write(r'\\%')
    f.write('\n\t')
    
    # Printing verses
    for i in tabspace:
        tex_Tabsubspaceverse(f, i)  
    f.write(r'\\%')
    f.write('\n')
    
    # Closing a Tabspace
    f.write(r'\end{minipage}%')
    f.write('\n')
    
         
    
