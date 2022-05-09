import itertools


def explode_pass(elems):
    depth = 0
    last_num_index = False
    for pos in range(len(elems)):
        if elems[pos] == ']':
            depth -= 1
        elif elems[pos] == '[':
            depth += 1
            if depth >= 5:
                exploded_left = elems[pos+1]
                exploded_right = elems[pos+2]
                next_num_index = False
                for g in range(pos+3, len(elems)):
                    if isinstance(elems[g], int):
                        elems[g] += exploded_right
                        break
                if last_num_index:
                    elems[last_num_index] += exploded_left
                for x in range(4):
                    del elems[pos]
                elems.insert(pos, 0)
                return True
        elif isinstance(elems[pos], int):
                last_num_index = pos
    return False


def split_pass(elems):
    last_num_index = False
    for pos in range(len(elems)):
        if isinstance(elems[pos], int):
            if elems[pos] >= 10:
                new_left = elems[pos] // 2
                new_right = elems[pos] - new_left
                elems.insert(pos+1, ']')
                elems.insert(pos+1, new_right)
                elems.insert(pos+1, new_left)
                elems[pos] = '['
                return True
            else:
                last_num_index = pos
    return False


def normalise(elems):
    while explode_pass(elems) or split_pass(elems):
        pass


def add(a, b):
    return ['['] + a + b + [']']


def magnitude(elems):
    if elems[0] == '[':
        left, remainder = magnitude(elems[1:])
        right, remainder = magnitude(remainder)
        return 3*left + 2*right, remainder[1:]
    if isinstance(elems[0], int):
        return elems[0], elems[1:]


def parse(inpt):
    inpt = inpt.replace('[', '[,').replace(']', ',]')
    inpt = inpt.split(',')
    return [int(c) if c.isnumeric() else c for c in inpt]


exprs = [parse(l.strip()) for l in open('day 18.txt').readlines()]

total = exprs[0]
for expr in exprs[1:]:
    total = add(total, expr)
    normalise(total)
mag, _ = magnitude(total)
print(f'Part 1: {mag}')

best_magnitude = 0
for one, two in itertools.permutations(exprs, 2):
    candidate = add(one, two)
    normalise(candidate)
    mag, _ = magnitude(candidate)
    best_magnitude = max(best_magnitude, mag)
print(f'Part 2: {best_magnitude}')