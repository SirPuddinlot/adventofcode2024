
total = 0
def process2(line):
    count = 0
    line2 = line.split()
    line2 = [int(i) for i in line2]
    def process(line, count):
        global total
        flag = line[0]-line[1]
        for i in range(len(line) - 1):
            diff = line[i]-line[i+1]
            #print("index ", i, )
            print("num ", line[i])
            if count < 2:
                if (abs(diff) > 3 ):
                    line.pop(i+1)
                    count += 1
                    process(line, count)
                    return
                elif (flag > 0 and diff < 0):
                    print("here")
                    line.pop(i+1)
                    count += 1
                    process(line, count)
                    return
                elif (flag < 0 and diff > 0):
                    print("here 2")
                    line.pop(i+1)
                    count += 1
                    process(line, count)
                    return
                elif (diff == 0):
                    line.pop(i+1)
                    count += 1
                    process(line, count)
                    return
            else:
                return
        total += 1
    process(line2, count)
with open("test.txt") as f:
    for line in f:
        process2(line)
print("ans ", total)