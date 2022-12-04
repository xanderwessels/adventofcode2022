import numpy as np
from pathlib import Path
f = open((Path(__file__).parent / "input.txt").resolve() , "r")

max_cal = np.zeros(3, dtype=int)
temp = 0
for line in f:
    if line != "\n":
        temp += int(line)
    elif temp > np.min(max_cal):
        max_cal[np.argmin(max_cal)] = temp
        temp = 0
    else:
        temp = 0 

f.close()
print(sum(max_cal))