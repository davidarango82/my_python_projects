
import re

f = open("C:/Users/david/my_python_projects/py4e/mbox.txt")
#s = input("Enter a regular expression:")
pat = "^X-DSPAM"
count = 0
for line in f:
    line = line.strip()
    res = re.findall(pat, line)
    if len(res)>0:
        # print(res)
        count += 1
print("there are",count,"lines matching the pattern.")