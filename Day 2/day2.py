f = open("/Users/joemoore/Documents/AdventOfCode/AdventOfCode2022/Day 2/input.txt","r")

data = f.readlines()
move1 = []
move2 = []

score = 0

for i in range(len(data)):
    temp = data[i].split()
    move1.append(temp[0])
    move2.append(temp[1])

    move2[i] = move2[i].replace("\n", "")

counter = 0

for i in range(len(move1)):
    if move1[i] == "A":
        if move2[i] == 'X':
            score = score + 3
        elif move2[i] == "Y":
            score = score + 4
        elif move2[i] == "Z":
            score = score + 8
    elif move1[i] == "B":
        if move2[i] == 'X':
            score = score + 1
        elif move2[i] == "Y":
            score = score + 5
        elif move2[i] == "Z":
            score = score + 9
    elif move1[i] == "C":
        if move2[i] == 'X':
            score = score + 2
        elif move2[i] == "Y":
            score = score + 6
        elif move2[i] == "Z":
            score = score + 7
    
    counter = counter + 1
    
print(counter)

#print(move2)

print(score)
