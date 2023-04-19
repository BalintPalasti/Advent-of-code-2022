TotalScore = 0

with open ('02.txt') as f:
    for line in f:
        lineClear = line.strip()
        match lineClear:
            case "A X": TotalScore += 3
            case "A Y": TotalScore += 4
            case "A Z": TotalScore += 8
            case "B X": TotalScore += 1
            case "B Y": TotalScore += 5
            case "B Z": TotalScore += 9
            case "C X": TotalScore += 2
            case "C Y": TotalScore += 6
            case "C Z": TotalScore += 7

print(TotalScore)