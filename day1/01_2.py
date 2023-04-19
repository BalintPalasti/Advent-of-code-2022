MaxCarriedCalories = [0, 0, 0]
ActualElvesCalories = 0
OldValue = 0

with open ('01.txt') as f:
    for line in f:
        if line != "\n":
            ActualElvesCalories += int(line)
        else:
            for i, element in enumerate(MaxCarriedCalories):
                if ActualElvesCalories > element:
                    oldval = element
                    MaxCarriedCalories[i] = ActualElvesCalories
                    ActualElvesCalories = oldval
            OldValue = 0
            ActualElvesCalories = 0

print(sum(MaxCarriedCalories))