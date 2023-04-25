import re

stacks = [
["B","L","D","T","W","C","F","M"],
['N','B','L'],
['J','C','H','T','L','V'],
['S','P','J','W'],
['Z','S','C','F','T','L','R'],
['W','D','G','B','H','N','Z'],
['F','M','S','P','V','G','C','N'],
['W','Q','R','J','F','V','C','Z'],
['R','P','M','L','H']
]


def numbersFromString(str):
    pieces = re.findall('\d+', str)       #list of 4 numbers
    return list(map(int, pieces))

def packing(pack_params):
    movement_No = pack_params[0]
    source_stack = pack_params[1] - 1
    destination_stack = pack_params[2] - 1

    for i in range(movement_No):
        stacks[destination_stack].append(stacks[source_stack][-1])
        stacks[source_stack].pop(-1)

def printLastElements(stack_list):
    for j in stack_list:
        print(j[-1])
    print('\n')

with open('05.txt') as f:
    for line in f:
        Packing_parameters = numbersFromString(line)
        packing(Packing_parameters)
    printLastElements(stacks)




