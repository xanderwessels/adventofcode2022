from pathlib import Path
f = open((Path(__file__).parent / "input.txt").resolve() , "r")

choice_score = {'A X': 3+0, 'A Y': 1+3, 'A Z': 2+6, 'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6, 'C X': 2+0, 'C Y': 3+3, 'C Z': 1+6}

total_score = 0
for line in f:
    total_score += choice_score[line[0:3]]

f.close()
print(total_score)