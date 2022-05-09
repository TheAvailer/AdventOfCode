data = []
with open("day 8.txt") as file:
    line = file.readline()
    while line:
        left = sorted(["".join(sorted(x)) for x in line.strip("\n").split("|")[0].split()], key=len)
        right = ["".join(sorted(x)) for x in line.strip("\n").split("|")[1].split()]
        data.append([left, right])
        line = file.readline()

def Substring(a, b):
    count = str()
    for character in a:
        if character in b:
            count += character
    return count

completetotal = 0
for problem in data:
    ten = problem[0]
    # 1,4,7,8
    setup = dict({ten[0]:1, ten [1]:7, ten[2]:4, ten[9]:8})
    fives = [ten[3], ten[4], ten[5]]
    sixes = [ten[6], ten[7], ten[8]]
    #6
    for index in range(len(sixes)):
        if len(Substring(ten[0], sixes[index])) == 1:
            setup[sixes[index]] = 6
            del(sixes[index])
            break

    #3
    for index in range(len(fives)):
        if len(Substring(ten[0], fives[index])) == 2:
            setup[fives[index]] = 3
            del(fives[index])
            break

    #9
    for index in range(len(sixes)):
        if len(Substring(ten[2], sixes[index])) == 4:
            setup[sixes[index]] = 9
            del(sixes[index])
            break

    #0
    setup[sixes[0]] = 0

    #2
    for index in range(len(fives)):
        if len(Substring(ten[2], fives[index])) == 2:
            setup[fives[index]] = 2
            del(fives[index])
            break

    #5
    setup[fives[0]] = 5

    total = 0
    for digit in problem[1]:
        total *= 10
        total += setup[digit]
    completetotal += total

print("P2:", completetotal)