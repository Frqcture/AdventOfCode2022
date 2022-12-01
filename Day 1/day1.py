def day1():
    f = open("/Users/joemoore/Documents/AdventOfCode/AdventOfCode2022/Day 1/data.txt", "r")

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

    elves.sort()

    print(elves[len(elves) - 1])

    print(elves[len(elves) - 1] + elves[len(elves) - 2] + elves[len(elves) - 3])

    f.close

day1()