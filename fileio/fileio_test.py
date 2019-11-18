import time
from pathlib import Path

mypath = Path(__file__).parent
print(mypath)
with open(str(mypath) + "\\" + "mytest.txt") as f:
    raw_string = f.readlines()

print("".join(raw_string))
time.sleep(5)