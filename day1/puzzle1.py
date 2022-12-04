max_cal = 0
from pathlib import Path
f = open((Path(__file__).parent / "input.txt").resolve() , "r")

temp = 0
for line in f:
    if line != "\n":
        temp += int(line)
    elif temp > max_cal:
        max_cal = temp
        temp = 0
    else:
        temp = 0 

f.close()
print(max_cal)