from time import perf_counter_ns
import re
import itertools
from dataclasses import dataclass, field
from math import prod

# filename = "day22_input.txt"
filename = "day 22.txt"


def read():
    with open(filename, "r") as f:
        lines = f.readlines()

    steps = []
    for line in lines:
        on_off = line.split()[0]
        matches = re.findall(r"([-\d]*\.\.[-\d]*)", line)
        matches = [tuple([int(r.split("..")[0]), int(r.split("..")[1]) + 1]) for r in matches]
        steps.append(tuple([on_off, matches]))
    return steps


def tuple_add(first, second):
    return tuple(a + b for a, b in zip(first, second))


def tuple_sub(first, second):
    return tuple(a - b for a, b in zip(first, second))


@dataclass(frozen=True)
class Cuboid:
    min_coords: tuple[int]
    max_coords: tuple[int]

    side_lengths: tuple[int] = field(repr=False, init=False)
    vertices: tuple[tuple[int]] = field(repr=False, init=False)
    midpoint: tuple[int] = field(repr=False, init=False)

    volume: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "side_lengths", tuple_sub(self.max_coords, self.min_coords))
        vertices = [self.min_coords, self.max_coords]
        dimensions = len(self.side_lengths)
        for i in range(dimensions):
            side = tuple(self.side_lengths[i] if cur == i else 0 for cur in range(dimensions))
            vertices.append(tuple_add(self.min_coords, side))

            side2 = tuple(
                self.side_lengths[i] if cur == i or cur == (i + 1) % dimensions else 0 for cur in range(dimensions))
            vertices.append(tuple_add(self.min_coords, side2))

        object.__setattr__(self, "vertices", tuple(vertices))
        object.__setattr__(self, "volume", prod(s for s in self.side_lengths))
        object.__setattr__(self, "midpoint", tuple(((a + b) / 2 for a, b in zip(self.min_coords, self.max_coords))))

    def contains(self, point: tuple[int]):
        for i in range(len(point)):
            if point[i] < self.min_coords[i] or point[i] >= self.max_coords[i]:
                return False
        return True


def cut_single(cube: Cuboid, plane):
    i, val = plane

    if val == cube.min_coords[i] or val == cube.max_coords[i]:
        # print("WTF")
        return {cube}

    if val < cube.min_coords[i] or val > cube.max_coords[i]:
        # print("WTF")
        # return {cube}
        return {cube}

    original_min = cube.min_coords
    original_max = cube.max_coords
    modified_min = tuple(val if j == i else original_min[j] for j in range(3))
    modified_max = tuple(val if j == i else original_max[j] for j in range(3))
    # make them still be min and max
    # modified_min, original_max = tuple(zip(*(sorted(pair) for pair in zip(modified_min, original_max))))
    # original_min, modified_max = tuple(zip(*(sorted(pair) for pair in zip(original_min, modified_max))))

    return {Cuboid(modified_min, original_max), Cuboid(original_min, modified_max)}


def cut(orig_cube: Cuboid, planes):
    cubes = {orig_cube}
    for plane in planes:
        new_cubes = set()
        for cube in cubes:
            new_cubes.update(cut_single(cube, plane))
        cubes = new_cubes
    return cubes


def part1():
    steps = read()

    # on_off, coords = steps[0]
    # current_cube = Cuboid(*zip(*coords))
    # print(current_cube)
    # print(cut(current_cube, ((0, 11), (1, 11))))
    # return

    on_cuboids = set()
    for on_off, coords in steps:
        current_cube = Cuboid(*zip(*coords))

        new_on_cuboids = set()
        # first add
        if not on_cuboids:
            on_cuboids = {current_cube}
            # print(sum(c.volume for c in on_cuboids))
            continue

        # print(f"{len(on_cuboids)=} {on_off=}")
        for cube_already_there in on_cuboids:

            cutting_planes = set()

            for vertex in current_cube.vertices:
                if cube_already_there.contains(vertex):
                    cutting_planes.update((i, vertex[i]) for i in range(3))

            # be careful with this
            if not cutting_planes:
                for vertex in cube_already_there.vertices:
                    if current_cube.contains(vertex):
                        cutting_planes.update((i, current_cube.min_coords[i]) for i in range(3))
                        cutting_planes.update((i, current_cube.max_coords[i]) for i in range(3))
            # till here

            if cutting_planes:
                # print()
                # print(f"{cube_already_there}")
                # print(f"{cutting_planes=}")
                new_cubes = cut(cube_already_there, cutting_planes)

                # how_many_cut_into = len(new_cubes)
                # removed = {nc for nc in new_cubes if current_cube.contains(nc.midpoint)}
                new_cubes = {nc for nc in new_cubes if not current_cube.contains(nc.midpoint)}
                # how_many_left = len(new_cubes)
                # print(f"removed {how_many_cut_into-how_many_left} cubes {removed=} {new_cubes=}")
                new_on_cuboids.update(new_cubes)
            else:
                new_on_cuboids.add(cube_already_there)
        # already subtracted its place from others, now add it if its also to be on!
        if on_off == "on":
            # print(f"adding {current_cube}")
            new_on_cuboids.add(current_cube)

        on_cuboids = new_on_cuboids
        # on_cuboids = {c for c in new_on_cuboids if c.volume > 0}

        print(on_cuboids)
        # print(f"\n!!!!!volume = {sum(c.volume for c in on_cuboids)}\n-------------\n")
    print(sum(c.volume for c in on_cuboids))
    # print(len(on_cuboids))


if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    # part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval / (10 ** 6):.2f} ms = {interval / (10 ** 9):.2f} s")