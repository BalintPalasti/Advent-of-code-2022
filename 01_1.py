MaxCarriedCalories = 0
ActualElvesCalories = 0

with open ('01.txt') as f:
    for line in f:
        if line != "\n":
            ActualElvesCalories += int(line)
        else:
            if ActualElvesCalories > MaxCarriedCalories:
                MaxCarriedCalories = ActualElvesCalories
            ActualElvesCalories = 0
        print(MaxCarriedCalories)
