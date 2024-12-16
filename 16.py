import math
from typing import Counter
from ec import nums, read_input


def parse(p):
    lines = read_input(p, split_lines=False)
    turns, cats = lines.split("\n\n")
    turns = nums(turns)
    cats = cats.split("\n")

    wheels = [[] for _ in range(len(turns))]
    for row in cats:
        for i in range(len(turns)):
            cat = row[4 * i : 4 * i + 4].strip()
            if len(cat) > 0:
                wheels[i].append(cat)

    return turns, wheels


turns, wheels = parse(1)
idxs = [0] * len(turns)
for _ in range(100):
    for i, t in enumerate(turns):
        idxs[i] = (idxs[i] + t) % len(wheels[i])

print(" ".join([wheels[i][j] for i, j in enumerate(idxs)]))


def coins(idxs, wheels):
    c = Counter()
    for i, j in enumerate(idxs):
        cat = wheels[i][j]
        c[cat[0]] += 1
        c[cat[2]] += 1
    return sum(max(t - 2, 0) for t in c.values())


turns, wheels = parse(2)
idxs = [0] * len(turns)
total = {0: 0}
cycle_length = math.lcm(*[len(wheel) for wheel in wheels])
for i in range(cycle_length):
    pulls = i + 1
    for i, t in enumerate(turns):
        idxs[i] = (idxs[i] + t) % len(wheels[i])
    total[pulls] = total[pulls - 1] + coins(idxs, wheels)

repeated = (202420242024 // cycle_length) * total[cycle_length]
rest = total[202420242024 % cycle_length]

print(repeated + rest)


def bfs_pulls(turns, wheels, comp):
    stack = [(tuple([0] * len(turns)), 256, 0)]
    seen = {}
    best = None
    while len(stack) > 0:
        idxs, pulls, total = stack.pop()
        if pulls == 0:
            best = comp(best, total) if best is not None else total
            continue

        key = (idxs, pulls)
        if key in seen and comp(total, seen[key]) == seen[key]:
            continue
        seen[key] = total

        for offset in range(-1, 2):
            new_idxs = list(idxs)
            for i, t in enumerate(turns):
                new_idxs[i] = (new_idxs[i] + t + offset) % len(wheels[i])

            new_total = total + coins(new_idxs, wheels)
            stack.append((tuple(new_idxs), pulls - 1, new_total))

    return best


turns, wheels = parse(3)
high = bfs_pulls(turns, wheels, max)
low = bfs_pulls(turns, wheels, min)
print(f"{high} {low}")
