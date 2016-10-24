


def PutTitlePreamble(f, song_name, raagam_name, taalam_name, arohanam_tex, avarohanam_tex):

    f.write(r'% Command to rotate right 90 degrees' + '\n')
    f.write(r'\newcommand*{\rotrt}[1]{\rotatebox{90}{#1}}' + '\n')
    f.write(r'' + '\n')
    f.write(r'% Command to rotate left 90 degrees' + '\n')
    f.write(r'\newcommand*{\rotlft}[1]{\rotatebox{-90}{#1}} ' + '\n')
    f.write(r'' + '\n')
    f.write(r'% Create the command for including the title page in the document' + '\n')
    f.write(r'\newcommand*{\titleBC}' + '\n')
    f.write(r'{%' + '\n')
    f.write(r'	\begingroup ' + '\n')
    f.write(r'% Center all text' + '\n')
    f.write(r'	\centering ' + '\n')
    f.write(r'%------------------------------------------------------------------------------------------------------' + '\n')
    f.write(r'%                               MAIN TITLE IN THIS SECTION BELOW' + '\n')
    f.write(r'' + '\n')
    f.write(r'	\def\CP{%' + '\n')
    f.write(r'	\textit{\Huge ' + song_name + r'}%' + '\n')
    f.write(r'	} % Title' + '\n')
    f.write(r'%------------------------------------------------------------------------------------------------------' + '\n')
    f.write(r'%' + '\n')
    f.write(r'	\settowidth{\unitlength}{\CP} % Set the width of the curly brackets to the width of the title' + '\n')
    f.write(r'	%' + '\n')
    f.write(r'	{%' + '\n')
    f.write(r'	\color{LightGoldenrod}%' + '\n')
    f.write(r'	\resizebox*{\unitlength}{\baselineskip}{\rotrt{$\}$}}' + '\n')
    f.write(r'} %' + '\n')
    f.write(r'%' + '\n')
    f.write(r'%' + '\n')
    f.write(r'\\[\baselineskip] % Print top curly bracket' + '\n')
    f.write(r'\textcolor{Sienna}{\CP} \\[\baselineskip] % Print title' + '\n')
    f.write(r'%' + '\n')
    f.write(r'%---------------------------------------------------------------------------------------------------------------------------------------' + '\n')
    f.write(r'{\color{Sienna}\Large Raagam: ' + raagam_name + r' \\ Talam: ' + taalam_name  r'} \\ % ENTER SECOND LINE OF TITLE' + '\n')
    f.write(r'%---------------------------------------------------------------------------------------------------------------------------------------' + '\n')
    f.write(r'{%' + '\n')
    f.write(r'\color{LightGoldenrod}' + '\n')
    f.write(r'\resizebox*{\unitlength}{\baselineskip}{\rotlft{$\}$}} % The second braces in the end of this line prints the bottom curly bracket. DO NOT MOVE THIS ' + '\n')
    f.write(r'} ' + '\n')
    f.write(r'%gin{scope}[titlepagecolor!40,line width=12pt,rounded corners=12pt]' + '\n')
    f.write(r'\vfill % Whitespace between the title and the author name' + '\n')
    f.write(r'' + '\n')
    f.write(r'\begin{flushleft}' + '\n')
    f.write(r'\vspace{100pt}' + '\n')
    f.write(r'\color{SlateBlue}' + '\n')
    f.write(r'\Large' + '\n')
    f.write(r'$\begin{array}{ll}' + '\n')
    f.write(r'\textbf{Arohanam:} &  ' + arohanam_tex + r'\\' + '\n')
    f.write(r'\textbf{Avarohanam:} &  ' + avarohanam_tex + r'\\' + '\n')
    f.write(r'\end{array}$' + '\n')
    f.write(r'' + '\n')
    f.write(r'\end{flushleft}' + '\n')
    f.write(r'' + '\n')
    f.write(r'\vfill % Whitespace ' + '\n')
    f.write(r'' + '\n')
    f.write(r'\endgroup}' + '\n')
    f.write(r'' + '\n')
    f.write(r'\newcommand\titlepagedecoration{%' + '\n')
    f.write(r'\begin{tikzpicture}[remember picture,overlay,shorten >= -10pt]' + '\n')
    f.write(r'' + '\n')
    f.write(r'\coordinate (aux1) at ([yshift=-15pt]current page.north east);' + '\n')
    f.write(r'\coordinate (aux2) at ([yshift=-410pt]current page.north east);' + '\n')
    f.write(r'\coordinate (aux3) at ([xshift=-4.5cm]current page.north east);' + '\n')
    f.write(r'\coordinate (aux4) at ([yshift=-150pt]current page.north east);' + '\n')
    f.write(r'' + '\n')
    f.write(r'\begin{scope}[titlepagecolor!40,line width=12pt,rounded corners=12pt]' + '\n')
    f.write(r'\draw' + '\n')
    f.write(r'  (aux1) -- coordinate (a)' + '\n')
    f.write(r'  ++(225:5) --' + '\n')
    f.write(r'  ++(-45:5.1) coordinate (b);' + '\n')
    f.write(r'\draw[shorten <= -10pt]' + '\n')
    f.write(r'  (aux3) --' + '\n')
    f.write(r'  (a) --' + '\n')
    f.write(r'  (aux1);' + '\n')
    f.write(r'\draw[opacity=0.6,titlepagecolor,shorten <= -10pt]' + '\n')
    f.write(r'  (b) --' + '\n')
    f.write(r'  ++(225:2.2) --' + '\n')
    f.write(r'  ++(-45:2.2);' + '\n')
    f.write(r'\end{scope}' + '\n')
    f.write(r'\draw[titlepagecolor,line width=8pt,rounded corners=8pt,shorten <= -10pt]' + '\n')
    f.write(r'  (aux4) --' + '\n')
    f.write(r'  ++(225:0.8) --' + '\n')
    f.write(r'  ++(-45:0.8);' + '\n')
    f.write(r'\begin{scope}[titlepagecolor!70,line width=6pt,rounded corners=8pt]' + '\n')
    f.write(r'\draw[shorten <= -10pt]' + '\n')
    f.write(r'  (aux2) --' + '\n')
    f.write(r'  ++(225:3) coordinate[pos=0.45] (c) --' + '\n')
    f.write(r'  ++(-45:3.1);' + '\n')
    f.write(r'\draw' + '\n')
    f.write(r'  (aux2) --' + '\n')
    f.write(r'  (c) --' + '\n')
    f.write(r'  ++(135:2.5) --' + '\n')
    f.write(r'  ++(45:2.5) --' + '\n')
    f.write(r'  ++(-45:2.5) coordinate[pos=0.3] (d);   ' + '\n')
    f.write(r'\draw ' + '\n')
    f.write(r'  (d) -- +(45:1);' + '\n')
    f.write(r'\end{scope}' + '\n')
    f.write(r'\end{tikzpicture}%' + '\n')
    f.write(r'}' + '\n')
    f.write(r'' + '\n')
    f.write(r'\definecolor{titlepagecolor}{cmyk}{1,.60,0,.40}' + '\n')