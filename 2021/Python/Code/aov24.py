from time import perf_counter_ns

with open("day 24.txt") as file:
    lines = file.read().split('\n')
data = list(zip([int(x.split()[-1]) for x in lines [4::18]],
                [int(x.split()[-1]) for x in lines [5::18]],
                [int(x.split()[-1]) for x in lines [15::18]]))


def recursive(parameters, order=lambda x: x, z = 0, number = ()):
    if not parameters:
        return number if z == 0 else None
    a, b, c = parameters[0]
    if a == 26:
        if not (1 <= (z%26) + b <= 9): return None
        return recursive(parameters[1:], order, z//a, number + ((z%26) + b,))
    for i in order(range(1, 10)):
        result = recursive(parameters[1:], order, z//a*26+i+c, number+(i,))
        if result is not None: return result


start = perf_counter_ns()

print("Part 1: ", recursive(data, order = reversed))

stop = perf_counter_ns()
interval = stop - start
print(f"\nTime taken: {interval} ns = {interval / (10 ** 6):.2f} ms = {interval / (10 ** 9):.2f} s")

print("Part 2: ", recursive(data))