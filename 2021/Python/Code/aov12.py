i = []
paths = []
track = [False, 'start']

for x in open("day 12.txt"):
    x = x.replace('\n','')
    i += [x.split('-')]


def next_cave(m):
    if m[-1] == 'end' : yield m
    else:
        for j in i:
            if j[0] == m[-1]:
                if j[1].islower():
                    if j[1] not in m:
                        yield from next_cave(m + [j[1]])
                    elif m[0] == False and j[1] != 'start': yield from next_cave([True] + m[1:] + [j[1]])
                else: yield from next_cave(m + [j[1]])
            elif j[1] == m[-1]:
                if j[0].islower():
                    if j[0] not in m :yield from next_cave(m + [j[0]])
                    elif m[0] == False and j[0] != 'start':
                        yield from next_cave([True] + m[1:] + [j[0]])
                else: yield from next_cave((m + [j[0]]))


for a in next_cave(track):
    paths.append(a)
print(len(paths))
