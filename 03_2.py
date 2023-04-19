def getCharsOfString (InputString):
    InputChars = []

    for i in range(int(len(InputString))):
        InputChars.append(InputString[i])

    return InputChars

def nextStorageCalculate (nextStorage):
    if nextStorage >= 2:
        nextStorage = 0
    else:
        nextStorage += 1
    return nextStorage

def prioNumberOfGroup (InputWord, nextStorage, BackpackOfGroup):
    BackpackOfGroup[nextStorage] = getCharsOfString(InputWord)
    if nextStorage >= 2:
        return findPriorityNumber(checkGroupPrority(BackpackOfGroup))
    return 0
    
def checkGroupPrority (BackpackOfGroup):
    for i in BackpackOfGroup[0]:
        for j in BackpackOfGroup[1]:
            if i == j:
                for k in BackpackOfGroup[2]:
                    if i == k:
                        return i

def findPriorityNumber (MyChar):
    MyCharNumber = ord(MyChar)
    if MyCharNumber >= 65 and MyCharNumber <= 90:
        MyCharNumber -= 38
    elif MyCharNumber >= 97 and MyCharNumber <= 122:
        MyCharNumber -= 96
    else:
        MyCharNumber = 0

    return MyCharNumber

SumPriorities = 0
BackpackOfGroup = [0,0,0]
nextStorage = 0

with open ('03.txt') as f:
    for line in f:
        lineClear = line.strip()
        SumPriorities += prioNumberOfGroup (lineClear, nextStorage, BackpackOfGroup)
        nextStorage = nextStorageCalculate (nextStorage)

print(SumPriorities)