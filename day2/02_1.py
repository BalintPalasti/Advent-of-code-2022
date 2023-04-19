TotalScore = 0

with open ('02.txt') as f:
    for line in f:
        lineClear = line.strip()
        match lineClear:
            case "A X": TotalScore += 4
            case "A Y": TotalScore += 8
            case "A Z": TotalScore += 3
            case "B X": TotalScore += 1
            case "B Y": TotalScore += 5
            case "B Z": TotalScore += 9
            case "C X": TotalScore += 7
            case "C Y": TotalScore += 2
            case "C Z": TotalScore += 6

print(TotalScore)