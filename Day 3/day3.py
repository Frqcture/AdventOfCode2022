f = open("/Users/joemoore/Documents/AdventOfCode/AdventOfCode2022/Day 3/data.txt","r")
data = f.readlines()

comp1 = []
comp2 = []

letters = []

for i in range(len(data)):
    for j in range(len(data[i])//2):
        comp1.append(data[i][j])
    for j in range(len(data[i])//2, len(data[i])):
        if data[i][j] != '\n':
            comp2.append(data[i][j])
        
    x = 0
    y = 0
    found = False
    while x < len(comp1) and found == False:
        y = 0
        while y < len(comp2) and found == False:

            if comp1[x] == comp2[y]:
                letters.append(comp1[x])
                found = True
            y = y + 1
        
        x = x + 1

    comp1 = []
    comp2 = []

score = 0

for i in range(len(letters)):
    if letters[i].isupper():
        score = score + ( ord(letters[i]) - 38 )
    if letters[i].islower():
        score = score + ( ord(letters[i]) - 96 )

print(score)

i = 0
pack1 = []
pack2 = []
pack3 = []

allletters = []

while i < len(data):
    print(i)
    for j in range(len(data[i])):
        pack1.append(data[i][j])
    for j in range(len(data[i+1])):
        pack2.append(data[i+1][j])
    for j in range(len(data[i+2])):
        pack3.append(data[i+2][j])
    i = i + 3

    pack1.remove('\n')
    pack2.remove('\n')

    print(pack1)
    print(pack2)
    print(pack3)

    oneandtwo = []
    all = []

    x = 0
    y = 0
    while x < len(pack1):
        y = 0
        while y < len(pack2):

            if pack1[x] == pack2[y]:
                oneandtwo.append(pack1[x])
            y = y + 1
        
        x = x + 1

    x = 0
    y = 0
    found = False
    while x < len(oneandtwo) and found == False:
        y = 0
        while y < len(pack3) and found == False:
            if oneandtwo[x] == pack3[y]:
                all.append(oneandtwo[x])
                found = True
            y = y + 1
        
        x = x + 1

    print(all)

    pack1 = []
    pack2 = []
    pack3 = []

    allletters.append(all[0])

    print(allletters)

n = 0

for i in range(len(allletters)):
    if allletters[i].isupper():
        n = n + ( ord(allletters[i]) - 38 )
    if allletters[i].islower():
        n = n + ( ord(allletters[i]) - 96 )

print(n)