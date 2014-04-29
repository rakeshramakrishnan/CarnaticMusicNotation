from Swaram import *
from Raagam import *

class Note(Swaram):
    def __init__(self, data = None, RaagamObj = None):
        ''' Can data be None??? '''
        ''' Do some magic relating to type of data being passed '''
        ''' At some point, it needs to create a swaram object?? '''
        super(Note, self).__init__()
        if type(data) == dict:
            self.MIDIToSwaram(data, RaagamObj)
        self.Transpose = 0
        
    def MIDIToSwaram(self, NoteDict, RaagamObj):
        self.MIDINote = NoteDict['note']
        self.NoteLength = NoteDict['duration']
        self.Octave = 0
        ''' Logic to convert MIDINote to Swaram '''
        # Higher octave (Mel Sthayi case)
        if self.MIDINote >= 36 and self.MIDINote <= 47:
            self.MIDINote = self.MIDINote + 24
            self.Octave = -2        
        elif self.MIDINote >= 48 and self.MIDINote <= 59:
            self.MIDINote = self.MIDINote + 12
            self.Octave = -1
        elif self.MIDINote >= 72 and self.MIDINote <= 83:
            self.MIDINote = self.MIDINote - 12
            self.Octave = 1
        elif self.MIDINote >= 84 and self.MIDINote <= 95:
            self.MIDINote = self.MIDINote - 24
            self.Octave = 2
        
        if self.MIDINote == 60:
            self.SwaramName = 'S'
            self.Swarasthanam = 1
        elif self.MIDINote == 61:
            self.SwaramName = 'R'
            self.Swarasthanam = 1
        elif self.MIDINote == 62:
            if RaagamObj.GetSwarasthanam('R') == 2:
                self.SwaramName = 'R'
                self.Swarasthanam = 2
            else:
                self.SwaramName = 'G'
                self.Swarasthanam = 1
        elif self.MIDINote == 63:
            if RaagamObj.GetSwarasthanam('R') == 3:
                self.SwaramName = 'R'
                self.Swarasthanam = 3
            else:
                self.SwaramName = 'G'
                self.Swarasthanam = 2
        elif self.MIDINote == 64:
            self.SwaramName = 'G'
            self.Swarasthanam = 3            
        elif self.MIDINote == 65:
            self.SwaramName = 'M'
            self.Swarasthanam = 1            
        elif self.MIDINote == 66:
            self.SwaramName = 'M'
            self.Swarasthanam = 2            
        elif self.MIDINote == 67:
            self.SwaramName = 'P'
            self.Swarasthanam = 2            
        elif self.MIDINote == 68:
            self.SwaramName = 'D'
            self.Swarasthanam = 1            
        elif self.MIDINote == 69:
            if RaagamObj.GetSwarasthanam('D') == 2:
                self.SwaramName = 'D'
                self.Swarasthanam = 2
            else:
                self.SwaramName = 'N'
                self.Swarasthanam = 1
        elif self.MIDINote == 70:
            if RaagamObj.GetSwarasthanam('D') == 3:
                self.SwaramName = 'D'
                self.Swarasthanam = 3
            else:
                self.SwaramName = 'N'
                self.Swarasthanam = 2         
        elif self.MIDINote == 71:
            self.SwaramName = 'N'
            self.Swarasthanam = 3
        elif self.MIDINote == 0:
            self.SwaramName = ','
            self.Swarasthanam = 1

        
         
            
            