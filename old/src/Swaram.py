
class Swaram(object):
    def __init__(self, swaram = None, Swarasthanam = None):
        self.SwaramName = swaram
        self.Swarasthanam = Swarasthanam
     
    def SetSwaram(self, SwaramName, Swarasthanam):
        self.SwaramName = SwaramName
        self.Swarasthanam = Swarasthanam
    
    def SetSwarasthanam(self, Swarasthanam):
        self.Swarasthanam = Swarasthanam
    
    def GetSwaram(self):
        swaramtemp = []
        swaramtemp.append(self.SwaramName)
        swaramtemp.append(self.Swarasthanam)
        return swaramtemp
    
    def GetSwarasthanam(self):
        return self.Swarasthanam
    
    def GetSwaramName(self):
        return self.SwaramName
    
    @staticmethod
    def is_swaram_valid(swar_char):
        return swar_char in ['S', 'R', 'G', 'M', 'P', 'D', 'N']