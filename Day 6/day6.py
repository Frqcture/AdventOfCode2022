f = open("/Users/joemoore/Documents/AdventOfCode/AdventOfCode2022/Day 6/data.txt","r")
data = f.readline()
lastChars = [0] * 14
for i in range(13,len(data)):
    for j in range(14):
        lastChars[j] = data[i-j]
    count = 0
    for char in lastChars:
        if lastChars.count(char) == 1:
            count += 1
    if count == 14:
        print(i+1)
        break