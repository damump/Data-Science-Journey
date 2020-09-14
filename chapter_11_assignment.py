import re

name = input("Enter File:")
if len(name) < 2 : name = "actual chapter11 assignment.txt"
handle = open(name)
total = None
numbers = list()
sums = list()
for line in handle:
    line = line.rstrip()
    y = re.findall("([0-9]+)" , line)
    if len(y) >= 1:
        numbers.append(y)
for number in numbers:
    for num in number:
        sums.append(num)
sums = list(map(int, sums))
print(sum(sums))
