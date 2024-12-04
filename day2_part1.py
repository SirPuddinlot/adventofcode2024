total = 0
def process(line):
    global total
    liner = line.split()
    liner = [int(i) for i in liner]
    # print(liner)
    flag = liner[0]-liner[1]
    for i in range(len(liner) - 1):
        diff = liner[i]-liner[i+1]
        if (abs(diff) > 3):
            return
        if (flag > 0 and diff < 0):
            return
        if (flag < 0 and diff > 0):
            return
        if (diff == 0):
            return
    total += 1

with open("test.txt") as f:
    for line in f:
        process(line)
print(total)
