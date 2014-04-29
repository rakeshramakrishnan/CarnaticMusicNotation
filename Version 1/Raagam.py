from Swaram import *
from Melakartha import *
import cPickle as pickle

class Raagam(object):
    def __init__(self, RaagamName = None, MelakarthaNum = None):
        self.RaagamName = RaagamName
        self.RaagamMelakartha = Melakartha(MelakarthaNum)
        self.Arohanam = None
        self.Avarohanam = None
        if RaagamName != None:
            self.PopulateRaagamInfo()
        
        
    def PopulateRaagamInfo(self):        
        # self.Arohanam = 
        # self.Avarohanam = 
        ''' Write code to set all the properties of the Raagam given Raagam name. This is done
            by scanning the Raagam database '''
        res = self.LoadRaagam()
        if res == False:
            print 'Raagam not found!!'
            print 'Please enter details for the Raagam'            
            self.SetRaagamInfo()
            self.SaveRaagam()
            

    def SetRaagamInfo(self):
        ''' Put code here to create new Raagam entry in the Raagam Database
            We should create new entry only if there is no Raagam by the existing name''' 
        self.Arohanam = []
        if self.RaagamMelakartha.MelakarthaNum == None:
            MelakarthaNum = raw_input('Enter the Melakartha Number: ')
            self.RaagamMelakartha = Melakartha(int(MelakarthaNum))
            
        SwaramNameListTemp = self.ParseInput(raw_input('Enter the Arohanam with spaces separating the swarams: '))
        
        for i in SwaramNameListTemp:
            for j in self.RaagamMelakartha.SwaramList:
                if len(i) == 2:
                    self.Arohanam.append(Swaram(i[0], int(i[1])))
                    break
                elif i == j.GetSwaramName():
                    self.Arohanam.append(j)
                    break
                
        self.Avarohanam = []
        SwaramNameListTemp = self.ParseInput(raw_input('Enter the Avarohanam with spaces separating the swarams: '))
        for i in SwaramNameListTemp:
            for j in self.RaagamMelakartha.SwaramList:
                if len(i) == 2:
                    self.Avarohanam.append(Swaram(i[0], int(i[1])))
                    break
                elif i == j.GetSwaramName():
                    self.Avarohanam.append(j)
                    break
        
        self.RaagamInfoTex()
        
    def ParseInput(self, inputstring):        
        SwaramNameListTemp = []
        swarflag = 0
        for i in range(0,len(inputstring)):
            if swarflag == 0 and inputstring[i].isalpha():
                swarflag = 1
                tempstr = ''
                tempstr = tempstr + inputstring[i]
            elif swarflag == 1 and inputstring[i].isdigit():
                swarflag = 0
                tempstr = tempstr + inputstring[i]
                SwaramNameListTemp.append(tempstr)
            elif swarflag == 1 and inputstring[i].isalpha():
                SwaramNameListTemp.append(tempstr)
                tempstr = ''
                tempstr = tempstr + inputstring[i]
        if swarflag == 1:
            SwaramNameListTemp.append(tempstr)
        
        return SwaramNameListTemp
        
    
    def RaagamInfoTex(self):
        self.ArohanamTex = '$'
        for i in range(0, len(self.Arohanam) - 1):
            if self.Arohanam[i].GetSwaramName() == 'P' or self.Arohanam[i].GetSwaramName() == 'S':
                self.ArohanamTex = self.ArohanamTex + self.Arohanam[i].GetSwaramName() + ' \: '
            else:
                self.ArohanamTex = self.ArohanamTex + self.Arohanam[i].GetSwaramName() + '_' + str(self.Arohanam[i].GetSwarasthanam()) + ' \: '
        self.ArohanamTex = self.ArohanamTex + '\HOct{S} \:'
        self.ArohanamTex = self.ArohanamTex + '$'
                
        self.AvarohanamTex = '$'
        self.AvarohanamTex = self.AvarohanamTex + '\HOct{S} \: '
        for i in range(1,len(self.Avarohanam)):
            if self.Avarohanam[i].GetSwaramName() == 'P' or self.Avarohanam[i].GetSwaramName() == 'S':
                self.AvarohanamTex = self.AvarohanamTex + self.Avarohanam[i].GetSwaramName() + ' \: '
            else:
                self.AvarohanamTex = self.AvarohanamTex + self.Avarohanam[i].GetSwaramName() + '_' + str(self.Avarohanam[i].GetSwarasthanam()) + ' \: '
        self.AvarohanamTex = self.AvarohanamTex + '$'  

        self.AroandAvaroTex = 'Arohanam:  & ' + self.ArohanamTex + '\n'
        self.AroandAvaroTex = self.AroandAvaroTex + 'Avarohanam: & ' + self.AvarohanamTex + '\n'
        
                        
    def SaveRaagam(self):        
        output = open('RaagamDB.txt', 'a')
        pickle.dump(self.__dict__, output)        
        output.close()
    
    
    def LoadRaagam(self):
        try:
            input = open('RaagamDB.txt', 'r')
        except IOError:
            input = open('RaagamDB.txt', 'w')
            return False
        try:
            tempRaagam = Raagam()
            while True:
                tempRaagam.__dict__ = pickle.load(input)
                if tempRaagam.RaagamName == self.RaagamName:
                    self.__dict__ = tempRaagam.__dict__
                    print 'Record found!!'
                    input.close()
                    return True
        except EOFError:
            input.close()
            return False            
        
        
    def GetSwarasthanam(self, swaramname):
        swarasthanam1 = None
        swarasthanam2 = None
        
        for i in self.Arohanam:
            if i.GetSwaramName() == swaramname:
                swarasthanam1 = i.GetSwarasthanam()
                break

                
        for i in self.Avarohanam:
            if i.GetSwaramName() == swaramname:
                swarasthanam2 = i.GetSwarasthanam()
                break
        
        
        if swarasthanam1 == None and swarasthanam2 == None:
            print 'Swar Not found!!'
            return None
        
        elif swarasthanam1 != None and swarasthanam2 == None:
            return swarasthanam1
        
        elif swarasthanam1 == None and swarasthanam2 != None:
            return swarasthanam2
        
        else:
            return min(swarasthanam1, swarasthanam2)

    
    def GetMelakarthaNum(self):
        ''' Write code to return the Melakartha number by scanning a database '''
        return self.RaagamMelakartha.MelakarthaNum
        
    def GetAroAndAvaroTex(self):
        ''' Write code here to get the Arohanam and Avarohanam by scanning Raagam database'''
        return self.AroandAvaroTex
        

if __name__ == '__main__':
    RaagamName = raw_input('Enter Raagam name: ')
    # MelakarthaNum = raw_input('Enter Melakartha number : ')
    Raag = Raagam(RaagamName)
    # Raag.PopulateRaagamInfo()
    
    # Raag.SetRaagamInfo()
    # Raag.SaveRaagam() 
    
        