from math import prod
from operator import gt, lt, eq
f = [sum, prod, min, max, None, gt, lt, eq]


class Bits:
    total = 0

    def __init__(self, s):
        self.s = s
        self.off = 0

    def handle(self):
        Bits.total += int(self.read(3), 2)
        type = int(self.read(3), 2)
        if type == 4: return self.get_literal()
        return f[type](self.get_res()) if type in range(5) else f[type](*self.get_res())

    def read(self, n):
        res = self.s[self.off:self.off+n]
        self.off += n
        return res
    def get_res(self):
        if self.read(1) =='0':
            res = []
            subp = Bits(self.read(int(self.read(15), 2)))
            while subp.off<len(subp.s):
                res.append(subp.handle())
            return res
        else:
            return [self.handle() for c in range(int(self.read(11),2))]

    def get_literal(self):
        c,e = '','1'
        while e != '0':
            e = self.read(1)
            t = self.read(4)
            c += t
        return int(c, 2)


aoc_input = open("day 16.txt").read()
s = bin(int(aoc_input, 16))[2:]
s = s.zfill(len(aoc_input)*4)
r = Bits(s).handle()
print('P1: ', Bits.total)
print('P2: ', r)

