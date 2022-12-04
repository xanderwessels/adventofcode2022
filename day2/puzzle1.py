from pathlib import Path
f = open((Path(__file__).parent / "input.txt").resolve() , "r")

choice_score = {'X': 1, 'Y': 2, 'Z': 3}

def score(line):
    score = 0
    score += choice_score[line[2]]
    if line[0] == "A":
        if line[2] == "Y":
            score += 6
        elif line[2] == "X":
            score += 3
    elif line[0] == "B":
        if line[2] == "Z":
            score += 6
        elif line[2] == "Y":
            score += 3           
    elif line[0] == "C":
        if line[2] == "X":
            score += 6
        elif line[2] == "Z":
            score += 3                        
    return score

total_score = 0
for line in f:
    total_score += score(line)

f.close()
print(total_score)