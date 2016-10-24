import cPickle as pickle

class Taalam(object):
    def __init__(self, taalam_name = None, taalam_split_up = None, length_laghu = None, swaras_per_aksharam = None):
        self.TaalamName = taalam_name
        self.TaalamSplitUp = taalam_split_up
        self.LengthLaghu = length_laghu
        self.SwarasPerAksharam = swaras_per_aksharam
        
        if self.TaalamName != None:
            self.PopulateTaalamInfo()
        
    
    def PopulateTaalamInfo(self):
        res = self.LoadTaalam()
        if res == False:
            print 'Raagam not found!!'
            print 'Please enter details for the Raagam'            
            self.SetTaalamInfo()
            self.SaveTaalam()
    
    
    def SetTaalamInfo(self):
        self.TaalamSplitUp = raw_input('Enter the Taalam split up: | for Laghu, 0 (zero) for Dhrutham and U for Anudhrtham: ')
        self.LengthLaghu = int(raw_input('Enter the length of laghu: '))
        self.SwarasPerAksharam = int(raw_input('Enter the number of swaras per aksharam: '))
        
        self.CalculateNumberOfAksharam()
        self.CalculateTabSpaceWidth()
        self.GetTaalamFormalName()
    
    
    def CalculateNumberOfAksharam(self):
        self.NumberOfAksharam = 0
        for i in self.TaalamSplitUp:
            if i == '|':
                self.NumberOfAksharam = self.NumberOfAksharam + self.LengthLaghu
            elif i == '0':
                self.NumberOfAksharam = self.NumberOfAksharam + 2
            elif i == 'U':
                self.NumberOfAksharam = self.NumberOfAksharam + 1
            
            # Since we have left and right pages
        self.NumberOfAksharam = self.NumberOfAksharam/2
            
    
    def CalculateTabSpaceWidth(self):
        self.TabSpaceWidth = 0.23
        if self.NumberOfAksharam == 4 and self.SwarasPerAksharam == 4:
            self.TabSpaceWidth = 0.23
        elif self.NumberOfAksharam == 3 and self.SwarasPerAksharam == 6:
            self.TabSpaceWidth = 0.30
        elif self.NumberOfAksharam == 3 and self.SwarasPerAksharam == 5:
            self.TabSpaceWidth = 0.27
        elif self.NumberOfAksharam == 4 and self.SwarasPerAksharam == 5:
            self.TabSpaceWidth = 0.20
        elif self.NumberOfAksharam == 4 and self.SwarasPerAksharam == 6:
            self.TabSpaceWidth = 0.18
        elif self.NumberOfAksharam == 3 and self.SwarasPerAksharam == 4:
            self.TabSpaceWidth = 0.23


    def GetTaalamFormalName(self):
        self.TaalamFormalName = ''
        if self.LengthLaghu == 3:
            self.TaalamFormalName = self.TaalamFormalName + 'Tisra'
        elif self.LengthLaghu == 4:
            self.TaalamFormalName = self.TaalamFormalName + 'Chatusra'
        elif self.LengthLaghu == 5:
            self.TaalamFormalName = self.TaalamFormalName + 'Khanda'
        elif self.LengthLaghu == 7:
            self.TaalamFormalName = self.TaalamFormalName + 'Misra'
        elif self.LengthLaghu == 9:
            self.TaalamFormalName = self.TaalamFormalName + 'Sankima'
        self.TaalamFormalName = self.TaalamFormalName + ' Jathi '
        
        if self.TaalamSplitUp == '|':
            self.TaalamFormalName = self.TaalamFormalName + 'Eka'
        elif self.TaalamSplitUp == '0|':
            self.TaalamFormalName = self.TaalamFormalName + 'Roopaka'
        elif self.TaalamSplitUp == '|00':
            self.TaalamFormalName = self.TaalamFormalName + 'Triputa'
        elif self.TaalamSplitUp == '|0|':
            self.TaalamFormalName = self.TaalamFormalName + 'Mattya'
        elif self.TaalamSplitUp == '|U0':
            self.TaalamFormalName = self.TaalamFormalName + 'Jhampa'
        elif self.TaalamSplitUp == '|0||':
            self.TaalamFormalName = self.TaalamFormalName + 'Dhruva'
        elif self.TaalamSplitUp == '||00':
            self.TaalamFormalName = self.TaalamFormalName + 'Ata'
        self.TaalamFormalName = self.TaalamFormalName + ' Taalam'
            
            
    def SaveTaalam(self):
        output = open('TaalamDB.txt', 'a')
        pickle.dump(self.__dict__, output)        
        output.close()
        
    
    def LoadTaalam(self):
        try:
            input = open('TaalamDB.txt', 'r')
        except IOError:
            input = open('TaalamDB.txt', 'w')
            return False
        try:
            tempTaalam = Taalam()
            while True:
                tempTaalam.__dict__ = pickle.load(input)
                if tempTaalam.TaalamName == self.TaalamName:
                    self.__dict__ = tempTaalam.__dict__
                    print 'Record found!!'
                    input.close()
                    return True
        except EOFError:
            input.close()
            return False     

            
    
        