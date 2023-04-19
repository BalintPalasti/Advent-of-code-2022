def getCharsOfString (InputString):
    HalfLengthOfString = int(len(InputString)/2)
    LengthOfString = 2*HalfLengthOfString
    InputChars = []

    for i in range(LengthOfString):
        InputChars.append(InputString[i])

    FirstHalf = InputChars[0:HalfLengthOfString]
    SecondHalf = InputChars[HalfLengthOfString:LengthOfString]

    return FirstHalf, SecondHalf      #Output: list of characters

def checkDuplication (InputString):
    FirstComparement, SecondComparement = getCharsOfString(InputString)
    for i in FirstComparement:
        for j in SecondComparement:
            if i == j:
                return i
    return "0"

def findPriorityNumber (InputString):
    MyCharNumber = ord(checkDuplication(InputString))
    if MyCharNumber >= 65 and MyCharNumber <= 90:
        MyCharNumber -= 38
    elif MyCharNumber >= 97 and MyCharNumber <= 122:
        MyCharNumber -= 96
    else:
        MyCharNumber = 0

    return MyCharNumber

SumPriorities = 0

with open ('03.txt') as f:
    for line in f:
        lineClear = line.strip()
        SumPriorities += findPriorityNumber(lineClear)

print(SumPriorities)
