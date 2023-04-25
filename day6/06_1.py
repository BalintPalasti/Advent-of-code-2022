
counter = 0
characters = ['1','2','3','4']

def create4ElementList(new_char):
    global characters
    global counter

    characters.append(new_char)
    characters.pop(0)
    counter += 1

def checkUniqe(list):
    if(len(set(list)) == len(list)):
        if counter <= 4:
            return False
        return True
    else:
        return False


with open('06.txt') as f:
    for input_word in f:
        for char in input_word:
            create4ElementList(char)
            if checkUniqe(characters):
                break
        print('The counter is: ', counter)
