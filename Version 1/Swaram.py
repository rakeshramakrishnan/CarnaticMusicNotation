
class Swaram(object):
    def __init__(self, swaram = None, swarasthanam = None):
        self.swaramname = swaram
        self.swarasthanam = swarasthanam
     
    def SetSwaram(self, swaramname, swarasthanam):
        self.swaramname = swaramname
        self.swarasthanam = swarasthanam
    
    def SetSwarasthanam(self, swarasthanam):
        self.swarasthanam = swarasthanam
    
    def GetSwaram(self):
        swaramtemp = []
        swaramtemp.append(self.swaramname)
        swaramtemp.append(self.swarasthanam)
        return swaramtemp
    
    def GetSwarasthanam(self):
        return self.swarasthanam
    
    def GetSwaramName(self):
        return self.swaramname