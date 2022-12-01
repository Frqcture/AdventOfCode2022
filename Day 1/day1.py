
f = open("data.txt", "r")

data = f.readlines()
elves = [0]
elfcounter = 0
for i in range(len(data) - 1):
    if data[i] == "\n":
        elfcounter = elfcounter + 1
        elves.append(0)
    else:
        thing = data[i].strip()
        elves[elfcounter] = elves[elfcounter] + int(thing)

biggest = 0
index = 0

for j in range(len(elves) - 1):
    if elves[j] > biggest:
        biggest = elves[j]
        index = j

print(str(biggest) + " " + str(j))

elves.sort()

print(elves[len(elves) - 1] + elves[len(elves) - 2] + elves[len(elves) - 3])

f.close