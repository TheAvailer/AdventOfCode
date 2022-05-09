from time import perf_counter_ns

start = perf_counter_ns()

def part1():
    grid = [list(l.strip()) for l in open("day 25.txt")]

    east = set()
    south = set()

    maximum_x = len(grid[0])
    maximum_y = len(grid)

    for y, l in enumerate(grid):
        for x, c in enumerate(l):
            if c == ">":
                east.add((x, y))
            elif c == "v":
                south.add((x, y))
    count = 0
    while True:
        newEast = set()
        newSouth = set()

        for e in east:
            newPos= ((e[0] + 1) % maximum_x, e[1])
            if newPos not in east and newPos not in south:
                newEast.add(newPos)
            else:
                newEast.add(e)

        for s in south:
            newPos = (s[0], (s[1] + 1) % maximum_y)
            if newPos not in south and newPos not in newEast:
                newSouth.add(newPos)
            else:
                newSouth.add(s)

        count += 1

        if newSouth == south and east == newEast:
            break
        south = newSouth
        east = newEast

    print(count)


part1()
stop = perf_counter_ns()
interval = stop - start
print(f"\nTime taken: {interval} ns = {interval / (10 ** 6):.2f} ms = {interval / (10 ** 9):.2f} s")
