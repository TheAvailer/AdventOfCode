import re
from time import perf_counter_ns


def doesLineIntersect(x0, x1, otherX0, otherX1):
    return x0 <= otherX0 <= x1 or x0 <= otherX1 <= x1 or otherX0 <= x0 <= otherX1 or otherX0 <= x1 <= otherX1


def getLineIntersect(pos0, pos1, otherPos0, otherPos1):
    assert doesLineIntersect(pos0, pos1, otherPos0, otherPos1)
    if otherPos0 <= pos0:
        r0 = pos0
    else:
        r0 = otherPos0
    if otherPos1 <= pos1:
        r1 = otherPos1
    else:
        r1 = pos1
    return r0, r1


class Cuboid:
    def __init__(self, x0, x1, y0, y1, z0, z1) -> None:
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1

        self.off = []

    def isIntersecting(self, other):
        return(
            doesLineIntersect(self.x0, self.x1, other.x0, other.x1)
            and doesLineIntersect(self.y0, self.y1, other.y0, other.y1)
            and doesLineIntersect(self.z0, self.z1, other.z0, other.z1)
        )

    def subtract(self, other):
        if self.isIntersecting(other):
            x = getLineIntersect(self.x0, self.x1, other.x0, other.x1)
            y = getLineIntersect(self.y0, self.y1, other.y0, other.y1)
            z = getLineIntersect(self.z0, self.z1, other.z0, other.z1)

            for o in self.off:
                o.subtract(other)

            self.off.append(Cuboid(x[0], x[1], y[0], y[1], z[0], z[1]))

    def volume(self):
        vol = (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1) - \
               sum([S.volume() for S in self.off])
        return vol

    def __repr__(self) -> str:
        temp = "" + str(self.x0) + ", " + str(self.x1) + ", " + str(self.y0) + ", " + str(self.y1) + ", " \
               + str(self.z0) + ", " + str(self.z1)

        return temp


def part2():
    start = perf_counter_ns()
    cuboids = []

    for t in open("day 22.txt").read().split("\n"):
        (x0, x1, y0, y1, z0, z1) = tuple(map(int, re.findall(r"-?\d+", t)))

        x_cube = Cuboid(x0, x1, y0, y1, z0, z1)
        for c in cuboids:
            c.subtract(x_cube)
        if "on" in t:
            cuboids.append(x_cube)

    print(sum(c.volume() for c in cuboids))
    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval / (10 ** 6):.2f} ms = {interval / (10 ** 9):.2f} s")


part2()
