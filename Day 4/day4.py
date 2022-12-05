f = open("/Users/joemoore/Documents/AdventOfCode/AdventOfCode2022/Day 4/data.txt", "r")

data = f.readlines()

counter = 0

for i in range(len(data)):
    temp = data[i].split(",")
    range1 = temp[0].split("-")
    range2 = temp[1].split("-")

    if int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]):
        counter = counter + 1

    elif int(range2[0]) <= int(range1[0]) and int(range2[1]) >= int(range1[1]):
        counter = counter + 1

print(counter)

count = 0

for i in range(len(data)):
    temp = data[i].split(",")
    range1 = temp[0].split("-")
    range2 = temp[1].split("-")

    if (int(range1[0]) >= int(range2[0])) and (int(range1[0]) <= int(range2[1])):
        count += 1
    elif (int(range1[1]) >= int(range2[0])) and (int(range1[1]) <= int(range2[1])):
        count += 1
    elif (int(range2[0]) >= int(range1[0])) and (int(range2[0]) <= int(range1[1])):
        count += 1
    elif (int(range2[1]) >= int(range1[0])) and (int(range2[1]) <= int(range1[1])):
        count += 1
    
print(count)