from Swaram import *
from Raagam import *
import MappingList

class Note(Swaram):
    def __init__(self, swaram_name = None, swarasthanam = None, note_length = None, octave = None, MIDI_note = None, 
        swarasthanam_display_flag = None, input_swaram = None, input_octave_char = None, latex_note_verse = '', latex_note = None, 
        input_swarasthanam_char = None):
        ''' Can data be None??? '''
        ''' Do some magic relating to type of data being passed '''
        ''' At some point, it needs to create a swaram object?? '''
        super(Note, self).__init__(swaram_name, swarasthanam)
        self.MIDINote = MIDI_note
        self.NoteLength = note_length
        self.Octave = octave
        
        self.InputSwaram = input_swaram
        self.InputSwarasthanamChar = input_swarasthanam_char
        self.InputOctaveChar = input_octave_char
        
        # Note: LatexNoteVerse is same as InputVerse. So only LatexNoteVerse is used
        self.LatexNoteVerse = latex_note_verse
        
        self.SwarasthanamDisplayFlag = swarasthanam_display_flag
        self.LatexNote = latex_note
        
        if self.SwaramName != None and self.Swarasthanam != None:
            self.MapEverything()
    

    def MapEverything(self): 
        mapping_list = []
        mapping_list = MappingList.GetMappingList()
        
        
        # print self.LatexSwaram
        
        # Case 1: Input through user:
        if self.InputSwaram != None:
            for i in mapping_list:
                if i[0][0] == self.SwaramName and i[0][-1] == str(self.Swarasthanam):
                    self.LatexSwaram = i[2]
                    break
            
            self.LatexNote = ''
            if self.Octave == 1:
                self.LatexNote = self.LatexNote + r'\HOct{'
                self.LatexNote = self.LatexNote + self.LatexSwaram[0]
                self.LatexNote = self.LatexNote + r'}'
            elif self.Octave == -1:
                self.LatexNote = self.LatexNote + r'\LOct{'
                self.LatexNote = self.LatexNote + self.LatexSwaram[0]
                self.LatexNote = self.LatexNote + r'}'
            elif self.Octave == 0:
                self.LatexNote = self.LatexNote + self.LatexSwaram[0]
                
            if self.SwarasthanamDisplayFlag== 1:
                self.LatexNote = self.LatexNote + r'\varnote{' + str(self.Swarasthanam) + r'}'
            
            # Assigning to MIDI Note
            base_note = {'S':60, 'R':61, 'G':62, 'M':65, 'P':67, 'D':68, 'N':69, ',':0}
            if base_note[self.SwaramName] == 0:
                self.MIDINote = 0
            else:
                self.MIDINote = base_note[self.SwaramName] + (self.Swarasthanam - 1)+ 12*self.Octave
                
        # Case 2: Input through MIDI:
        # Hence need to fill in input character and Latex output
        elif self.MIDINote != None:
            for i in mapping_list:
                if i[0][0] == self.SwaramName and i[0][-1] == str(self.Swarasthanam):
                    self.InputSwaram = i[1]
                    self.LatexSwaram = i[2]
                    break
            
            self.LatexNote = ''
            if self.Octave == 1:
                self.LatexNote = self.LatexNote + r'\HOct{'
                self.LatexNote = self.LatexNote + self.LatexSwaram[0]
                self.LatexNote = self.LatexNote + r'}'
                self.InputOctaveChar = '\''
            elif self.Octave == -1:
                self.LatexNote = self.LatexNote + r'\LOct{'
                self.LatexNote = self.LatexNote + self.LatexSwaram[0]
                self.LatexNote = self.LatexNote + r'}'
                self.InputOctaveChar = '.'
            elif self.Octave == 0:
                self.LatexNote = self.LatexNote + self.LatexSwaram[0]
            
            if self.SwarasthanamDisplayFlag == 1:
                self.LatexNote = self.LatexNote + r'\varnote{' + str(self.Swarasthanam) + r'}'
                self.InputSwarasthanamChar = str(self.Swarasthanam)
            
            
    
    @classmethod
    def MIDIToSwaram(cls, MIDI_note_dict, raagam_obj):
        MIDI_note = MIDI_note_dict['note']
        note_length = MIDI_note_dict['duration']
        latex_note_verse = ''
        if MIDI_note_dict.has_key('verse'):
            latex_note_verse = MIDI_note_dict['verse']
        octave = 0        
        ''' Logic to convert MIDI_note to Swaram '''
        # Higher octave (Mel Sthayi case)
        if MIDI_note >= 36 and MIDI_note <= 47:
            MIDI_note = MIDI_note + 24
            octave = -2        
        elif MIDI_note >= 48 and MIDI_note <= 59:
            MIDI_note = MIDI_note + 12
            octave = -1
        elif MIDI_note >= 72 and MIDI_note <= 83:
            MIDI_note = MIDI_note - 12
            octave = 1
        elif MIDI_note >= 84 and MIDI_note <= 95:
            MIDI_note = MIDI_note - 24
            octave = 2

        # Assigning swarams from MIDI note
        if MIDI_note == 60:
            swaram_name = 'S'
            swarasthanam = 1
        elif MIDI_note == 61:
            swaram_name = 'R'
            swarasthanam = 1
        elif MIDI_note == 62:
            if raagam_obj.GetSwarasthanam('R') == 2:
                swaram_name = 'R'
                swarasthanam = 2
            else:
                swaram_name = 'G'
                swarasthanam = 1
        elif MIDI_note == 63:
            if raagam_obj.GetSwarasthanam('R') == 3:
                swaram_name = 'R'
                swarasthanam = 3
            else:
                swaram_name = 'G'
                swarasthanam = 2
        elif MIDI_note == 64:
            swaram_name = 'G'
            swarasthanam = 3            
        elif MIDI_note == 65:
            swaram_name = 'M'
            swarasthanam = 1            
        elif MIDI_note == 66:
            swaram_name = 'M'
            swarasthanam = 2            
        elif MIDI_note == 67:
            swaram_name = 'P'
            swarasthanam = 1            
        elif MIDI_note == 68:
            swaram_name = 'D'
            swarasthanam = 1            
        elif MIDI_note == 69:
            if raagam_obj.GetSwarasthanam('N') == 1:
                swaram_name = 'N'
                swarasthanam = 1
            else:
                swaram_name = 'D'
                swarasthanam = 2
        elif MIDI_note == 70:
            if raagam_obj.GetSwarasthanam('N') == 2:
                swaram_name = 'N'
                swarasthanam = 2                 
            else:        
                swaram_name = 'D'
                swarasthanam = 3
        elif MIDI_note == 71:
            swaram_name = 'N'
            swarasthanam = 3
        elif MIDI_note == 0:
            swaram_name = ','
            swarasthanam = 0
        
        # Check if swarasthanam needs to be printed
        if raagam_obj.GetSwarasthanam(swaram_name) == swarasthanam:
            swarasthanam_display_flag = 0
        else:
            swarasthanam_display_flag = 1
        
       
        Note1 = cls(swaram_name = swaram_name, swarasthanam = swarasthanam, note_length = note_length, octave = octave, MIDI_note = MIDI_note, 
                    swarasthanam_display_flag = swarasthanam_display_flag, latex_note_verse = latex_note_verse)
        return Note1
        
        
    @classmethod
    def InputToSwaram(cls, input_note_dict, raagam_obj):
        
        input_swaram = input_note_dict['swaram']
        octave = input_note_dict['octave']
        input_octave_char = None
        if input_note_dict.has_key('octavechar'):
            input_octave_char = input_note_dict['octavechar']
        
        input_swarasthanam_char = None
        if input_note_dict.has_key('swarasthanam'):
            input_swarasthanam_char = input_note_dict['swarasthanam']
        
        note_length = input_note_dict['length']
        latex_note_verse = input_note_dict['verse']
        
        mapping_list = []
        mapping_list = MappingList.GetMappingList()
        
        # Check if latex_note_verse and note_length are None by mistake:
        if latex_note_verse == None:
            latex_note_verse = ''
        
        if note_length == None:
            note_length = 1
        
        for i in mapping_list:
            if input_swarasthanam_char != None:
                if i[1][0] == input_swaram and i[1][-1] == input_swarasthanam_char:
                    swaram_name = i[0][0]
                    swarasthanam = int(i[1][1])
                    swarasthanam_display_flag = 1
                    break
            else:
                if i[1][0] == input_swaram:
                    swaram_name = i[0][0]
                    swarasthanam = raagam_obj.GetSwarasthanam(swaram_name)
                    if swarasthanam == 0:
                        if swaram_name != ',':
                            swarasthanam = 1
                            swarasthanam_display_flag = 1
                        else:
                            swarasthanam = 0
                            swarasthanam_display_flag = 0
                    else:
                        swarasthanam_display_flag = 0
                    break
        if swaram_name == 'S' or swaram_name == 'P':
            swarasthanam = 1
            swarasthanam_display_flag = 0
        # elif swaram_name == ','
        
        Note1 = cls(swaram_name = swaram_name, swarasthanam = swarasthanam, note_length = note_length, octave = octave, input_swaram = input_swaram, 
                    input_swarasthanam_char = input_swarasthanam_char, input_octave_char = input_octave_char,
                    swarasthanam_display_flag = swarasthanam_display_flag, latex_note_verse = latex_note_verse)
        return Note1        
            

