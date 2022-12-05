stacks = [[],[],[],[],[],[],[],[],[]]
stacks[0].extend(("J","H","P","M","S","F","N","V"))
stacks[1].extend(("S","R","L","M","J","D","Q"))
stacks[2].extend(("N","Q","D","H","C","S","W","B"))
stacks[3].extend(("R","S","C","L"))
stacks[4].extend(("M","V","T","P","F","B"))
stacks[5].extend(("T","R","Q","N","C"))
stacks[6].extend(("G","V","R"))
stacks[7].extend(("C","Z","S","P","D","L","R"))
stacks[8].extend(("D","S","J","V","G","P","B","F"))

# stacks = [[],[],[]]
# stacks[0].extend(("Z","N"))
# stacks[1].extend(("M","C","D"))
# stacks[2].extend(("P"))

f = open("/Users/joemoore/Documents/AdventOfCode/AdventOfCode2022/Day 5/data.txt","r")

data = f.readlines()

o = open("output.txt", "w")

for i in range(len(data)):
    split1 = data[i].split(" from ")
    numelements = split1[0]
    fromto = split1[1]
    split2 = fromto.split(" to ")
    popfrom = split2[0]
    pushto = split2[1]
    numelements = numelements.replace("move ","")

    for j in range(int(numelements)):
        temp = stacks[int(popfrom)-1].pop()
        stacks[int(pushto)-1].append(temp)
    

print(stacks[0][len(stacks[0])-1] + stacks[1][len(stacks[1])-1] + stacks[2][len(stacks[2])-1] + stacks[3][len(stacks[3])-1] + stacks[4][len(stacks[4])-1] + stacks[5][len(stacks[5])-1] + stacks[6][len(stacks[6])-1] + stacks[7][len(stacks[7])-1] + stacks[8][len(stacks[8])-1])

# print(stacks[0][len(stacks[0])-1] + stacks[1][len(stacks[1])-1] + stacks[2][len(stacks[2])-1])

stacks[0].extend(("J","H","P","M","S","F","N","V"))
stacks[1].extend(("S","R","L","M","J","D","Q"))
stacks[2].extend(("N","Q","D","H","C","S","W","B"))
stacks[3].extend(("R","S","C","L"))
stacks[4].extend(("M","V","T","P","F","B"))
stacks[5].extend(("T","R","Q","N","C"))
stacks[6].extend(("G","V","R"))
stacks[7].extend(("C","Z","S","P","D","L","R"))
stacks[8].extend(("D","S","J","V","G","P","B","F"))

crates = []

for i in range(len(data)):
    split1 = data[i].split(" from ")
    numelements = split1[0]
    fromto = split1[1]
    split2 = fromto.split(" to ")
    popfrom = split2[0]
    pushto = split2[1]
    numelements = numelements.replace("move ","")

    for j in range(int(numelements)):
        crates.append(stacks[int(popfrom)-1].pop())

    for j in range(int(numelements)):
        stacks[int(pushto)-1].append(crates.pop())

    crates = []

print(stacks[0][len(stacks[0])-1] + stacks[1][len(stacks[1])-1] + stacks[2][len(stacks[2])-1] + stacks[3][len(stacks[3])-1] + stacks[4][len(stacks[4])-1] + stacks[5][len(stacks[5])-1] + stacks[6][len(stacks[6])-1] + stacks[7][len(stacks[7])-1] + stacks[8][len(stacks[8])-1])