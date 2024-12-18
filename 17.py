from collections import defaultdict
import heapq
import math
from ec import read_input


def parse(p, max_weight=math.inf):
    lines = read_input(p)

    stars = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                stars.append((x, y))

    adj = defaultdict(list)
    for i in range(len(stars)):
        for j in range(i + 1, len(stars)):
            ix, iy = stars[i]
            jx, jy = stars[j]
            md = abs(ix - jx) + abs(iy - jy)
            if md < max_weight:
                adj[stars[i]].append((md, stars[j]))
                adj[stars[j]].append((md, stars[i]))

    return stars, adj


def prim(p):
    stars, adj = parse(p)

    total_weight = 0
    seen = {stars[0]}
    frontier = []
    for w, n in adj[stars[0]]:
        heapq.heappush(frontier, (w, n))

    while len(seen) < len(stars):
        w, curr = heapq.heappop(frontier)
        if curr in seen:
            continue
        seen.add(curr)
        total_weight += w
        for w, pos in adj[curr]:
            if pos not in seen:
                heapq.heappush(frontier, (w, pos))

    return total_weight + len(stars)


print(prim(1))
print(prim(2))

stars, adj = parse(3, max_weight=6)

remaining = set(stars)
sizes = []
while len(remaining) > 0:
    start = remaining.pop()
    total_weight = 0
    seen = {start}
    frontier = []
    for w, n in adj[start]:
        heapq.heappush(frontier, (w, n))

    while len(frontier) > 0:
        w, curr = heapq.heappop(frontier)
        if curr in seen:
            continue
        seen.add(curr)
        total_weight += w
        for w, pos in adj[curr]:
            if pos not in seen:
                heapq.heappush(frontier, (w, pos))

    remaining.difference_update(seen)
    sizes.append(total_weight + len(seen))

total = 1
for n in sorted(sizes)[-3:]:
    total *= n

print(total)
