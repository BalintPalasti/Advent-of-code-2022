import re

def numbersFromString(str):
    return re.findall('\d+', str)       #list of 4 numbers

def decideIfOverlaps(numbers):
    n1 = int(numbers[0])
    n2 = int(numbers[1])
    n3 = int(numbers[2])
    n4 = int(numbers[3])
    if n1 <= n3 and n2 >= n3:
        return 1
    if n3 <= n1 and n4 >= n1:
        return 1
    return 0

sumOverlaps = 0

with open('04.txt') as f:
    for line in f:
        sumOverlaps += decideIfOverlaps(numbersFromString(line))

print("Total:", sumOverlaps)