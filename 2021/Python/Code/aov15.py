from collections import defaultdict
from math import inf
import heapq
from time import perf_counter_ns
start = perf_counter_ns()




D1 = [[int(i) for i in line] for line in open("day 15.txt").read().splitlines()]
D2 = [[(D1[j%len(D1)][i%len(D1)] + int(i/len(D1)) + int(j/len(D1)) - 1) % 9 + 1
       for i in range(len(D1) * 5)] for j in range(len(D1) * 5)]


def shortestPath(data):
    risk = defaultdict(lambda: inf, {(0, 0): 0})
    visited = defaultdict(lambda: False)
    heapq.heappush(Q := [], (0, (0, 0)))
    while Q:
        x = heapq.heappop(Q)[1]
        visited[x] = True
        for n in [p for p in [(x[0]-1, x[1]), (x[0]+1, x[1]), (x[0], x[1]-1), (x[0], x[1]+1)]
                  if p[0] in range(len(data)) and p[1] in range(len(data))]:
            if not visited[n]:
                newRisk = risk[x] + data[n[0]][n[1]]
                if risk[n] > newRisk:
                    risk[n] = newRisk
                    heapq.heappush(Q, (newRisk, n))
    return risk[(len(data)-1, len(data)-1)]


answer = shortestPath(D1);

print("P1: ", shortestPath(D1))
print("P2: ", shortestPath(D2))
stop = perf_counter_ns()
interval = stop - start
print(f"\nTime taken: {interval} ns = {interval / (10 ** 6):.2f} ms = {interval / (10 ** 9):.2f} s")
