def GetMappingList():
    with open('NoteMapper.txt', 'r') as f:
        mapping_list = []
        for line in f:
            if line.startswith('#') == False:
                NoteListTemp = []
                quoteflag = 0
                for i in range(0,len(line)):
                    if quoteflag == 0 and (line[i]== '\'' or line[i] == '\"'):
                        quoteflag = 1
                        tempstr = ''
                    elif quoteflag == 1 and (line[i].isalnum() or line[i] == '/' or line[i] == ','): 
                        tempstr = tempstr + line[i]
                    elif quoteflag == 1 and (line[i]== '\'' or line[i] == '\"'):
                        quoteflag = 0
                        NoteListTemp.append(tempstr)
                        tempstr = ''
                if quoteflag == 1:
                    quoteflag = 0
                    NoteListTemp.append(tempstr)
                mapping_list.append(NoteListTemp)
    
    # The mapping information has been obtained
    return mapping_list