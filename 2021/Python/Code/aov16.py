from functools import reduce


def parse_bin(string, values, val = '', op = None):
    v, t, string = int(string[:3], 2), int(string[3:6], 2), string[6:]
    versions.append(v)
    if t == 4:
        while op != '0':
            op, val, string = string[0], val + string[1:5], string[5:]
        return string, values + [int(val, 2)]
    length = lengths[string[0]](string)
    if string[0] == '0':
        copy, string = string[16 : 16 + length], string[16 + length:]
        while len(copy) > 5:
            copy, v = parse_bin(copy, [])
            values += v
    else:
        string = string[12:]
        for e in range(length):
            string, v = parse_bin(string, [])
            values += v
    return string, [types[t](values)]


with open("day 16.txt", 'r') as file:
    raw = file.read()
    data = bin(int(raw, 16))[2:].zfill(len(raw) * 4)
    versions, values = [], []
    lengths = {'0': lambda x: int(x[1:16], 2),
               '1': lambda x: int(x[1:12], 2)}
    types = {0: lambda values: sum(values),
             1: lambda values: reduce(lambda x, y: x*y, values),
             2: lambda values: min(values),
             3: lambda values: max(values),
             5: lambda values: int(values[0] > values[1]),
             6: lambda values: int(values[0] < values[1]),
             7: lambda values: int(values[0] == values[1])}
    while len(data) > 11:
        data, values = parse_bin(data, [])
    print('P1: ',sum(versions))
    print('P2: ', values[0])