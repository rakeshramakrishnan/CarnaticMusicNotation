from Note import *

class TabSubSpace(object):
    def __init__(self, note_latex, verse_latex, fast_flag):
        self.LatexFunctionName = r'\TBSSpace'
        self.LatexFunctionDefinition = r'\newcommand{\TBSspace}[1]{\makebox[0.20\linewidth][c]{$\text{#1}$}}' + '\n\n'
        self.LatexNote = self.LatexFunctionName + '{' + note_latex + '}%'
        self.LatexVerse = self.LatexFunctionName + '{' + verse_latex + '}%'
        self.FastFlag = fast_flag
    
    def GetLatexNote(self):
        return self.LatexNote
    
    def GetLatexVerse(self):
        return self.LatexVerse
    
    def GetFastFlag(self):
        return self.FastFlag
