# from itertools import chain
import sys
from Swaram import *

class Melakartha(object):
    def __init__(self, MelakarthaNum = None):
        self.MelakarthaNum = MelakarthaNum
        self.Sa = Swaram('S', 1)
        self.Ri = Swaram('R')
        self.Ga = Swaram('G')
        self.Ma = Swaram('M')
        self.Pa = Swaram('P', 1)
        self.Da = Swaram('D')
        self.Ni = Swaram('N')
        if MelakarthaNum != None:
            self.SetSwarasthanam()        
    
    def SetSwarasthanam(self):
        ''' Define logic to assign RGMDN values to Melakartha
            Here, RGMDN shall be a list containing 5 numbers each
            corresponding to the variation of the respective swara
            No need to create an object of swara within it '''
        self.SwaramList = []
        
        if self.MelakarthaNum > 36:
            MelakarthaNumtemp = self.MelakarthaNum - 36
        else:
            MelakarthaNumtemp = self.MelakarthaNum
        
        self.RaagaPosInChakra = int(MelakarthaNumtemp)%6
        
        self.Group1 = [1, 2, 3, 4, 5, 6]
        self.Group2 = [7, 8, 9, 10, 11, 12]
        self.Group3 = [13, 14, 15, 16, 17, 18]
        self.Group4 = [19, 20, 21, 22, 23, 24]
        self.Group5 = [25, 26, 27, 28, 29, 30]
        self.Group6 = [31, 32, 33, 34, 35, 36]
        
        if MelakarthaNumtemp in self.Group1:
            self.Ri.SetSwarasthanam(1)
            self.Ga.SetSwarasthanam(1)
            self.Chakra = 1
        elif MelakarthaNumtemp in self.Group2:
            self.Ri.SetSwarasthanam(1)
            self.Ga.SetSwarasthanam(2)
            self.Chakra = 2
        elif MelakarthaNumtemp in self.Group3:
            self.Ri.SetSwarasthanam(1)
            self.Ga.SetSwarasthanam(3)
            self.Chakra = 3
        elif MelakarthaNumtemp in self.Group4:
            self.Ri.SetSwarasthanam(2)
            self.Ga.SetSwarasthanam(2)
            self.Chakra = 4
        elif MelakarthaNumtemp in self.Group5:
            self.Ri.SetSwarasthanam(2)
            self.Ga.SetSwarasthanam(3)
            self.Chakra = 5
        elif MelakarthaNumtemp in self.Group6:
            self.Ri.SetSwarasthanam(3)
            self.Ga.SetSwarasthanam(4)
            self.Chakra = 6
        
        if self.MelakarthaNum > 36:
            self.Ma.SetSwarasthanam(2)
            self.Chakra = self.Chakra + 6
        else:
            self.Ma.SetSwarasthanam(1)
        

        if self.RaagaPosInChakra in [1, 2, 3]:
            self.Da.SetSwarasthanam(1)
        elif self.RaagaPosInChakra in [4, 5]:
            self.Da.SetSwarasthanam(2)
        elif self.RaagaPosInChakra in [0]:
            self.Da.SetSwarasthanam(3)

        if self.RaagaPosInChakra in [1]:
            self.N.SetSwarasthanam(1)
        elif self.RaagaPosInChakra in [2, 4]:
            self.Ni.SetSwarasthanam(2)
        elif self.RaagaPosInChakra in [3, 5, 0]:
            self.Ni.SetSwarasthanam(3)
            
        self.SwaramList = [self.Sa, self.Ri, self.Ga, self.Ma, self.Pa, 
                           self.Da, self.Ni]
                
    def GetSwaramList(self):
        return self.SwaramList
    
    # def __str__(self):
        # return "%s: %s" % (se
        

# Debugging
if __name__ == '__main__':
    MelakarthaNum = int(sys.argv[1])
    Melakartha_object = Melakartha(MelakarthaNum)
    SwarList = Melakartha_object.GetSwaramList()
    print SwarList
    
        
        
        
