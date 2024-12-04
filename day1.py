# Online Python - IDE, Editor, Compiler, Interpreter
from collections import defaultdict
from collections import Counter

list1 = []
list2 = []
with open("./aoc1.txt", "r") as f:
    for line in f:
        x = line.split()
        list1.append(x[0])
        list2.append(x[1])
#problem 1 part 1
list1.sort()
list2.sort()
total = 0
for i, j in zip(list1,list2):
    total += abs(int(i)-int(j))
print(total)

#problem 2 part 2
dick1 = Counter(list1)
dick2 = Counter(list2)
total = 0
for key, value in dick1.items():
    total += (int(key) * value * int(dick2[key]))
print(total)
