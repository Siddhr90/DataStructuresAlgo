# bottom up
# we are implementing matrix here

def minStringEdit(string1, string2, tempDict):
    for i1 in range(len(string1)+1):
        tempDict[str(i1)+'0'] = i1

    for i2 in range(len(string2)+1):
        tempDict['0'+str(i2)] = i2

    for i1 in range(1,len(string1)+1):
        for i2 in range(1, len(string2)+1):
            if string1[i1-1] == string2[i2-1]:
                tempDict[str(i1)+str(i2)] = tempDict[str(i1-1)+str(i2-1)]
            else:
                dictD = tempDict[str(i1-1)+str(i2)]
                dictA = tempDict[str(i1) + str(i2-1)]
                dictR = tempDict[str(i1 - 1) + str(i2-1)]
                tempDict[str(i1)+str(i2)] = 1 + min(dictA, dictD, dictR)

    return tempDict[str(len(string1))+str(len(string2))]

print(minStringEdit(" ","bik", {}))


