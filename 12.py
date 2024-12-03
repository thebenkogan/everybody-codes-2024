import math
from ec import nums, read_input


def load(p):
    lines = read_input(p)
    grid = [[c for c in line] for line in lines]
    cannons = []
    targets = []
    for y, line in enumerate(grid):
        y = len(grid) - 1 - y
        for x, c in enumerate(line):
            if c in ["A", "B", "C"]:
                cannons.append((x, y))
            if c == "T":
                targets.append(((x, y), 1))
            if c == "H":
                targets.append(((x, y), 2))
    return grid, cannons, targets


def can_hit(cannon, target):
    cx, cy = cannon
    tx, ty = target

    # special case: target trajectory is too high
    if abs(ty - cy) > abs(tx - cx):
        return False, 0, 0

    # special case: cannon is in line with target
    if tx - cx == ty - cy:
        return True, tx - cx, tx - cx

    t = 0
    diff = abs(ty - cy)
    if ty < cy:
        tx -= diff
        ty += diff
        t = diff
    elif ty > cy:
        rise = ty - cy
        # hit along the horizontal part of the trajectory
        if rise < (tx - cx) < 2 * rise:
            mv = 2 * rise - (tx - cx)
            tx += mv
            t -= mv

        tx += diff
        ty -= diff
        t -= diff

    t += tx - cx
    return (tx - cx) % 3 == 0, (tx - cx) / 3, t


def score(grid, cannons, targets):
    total = 0
    for (x, y), hits in targets:
        for cx, cy in cannons:
            good, power, _ = can_hit((cx, cy), (x, y))
            if good:
                total += (ord(grid[len(grid) - cy - 1][cx]) - 64) * power * hits
                break
    return total


grid, cannons, targets = load(1)
print(score(grid, cannons, targets))

grid, cannons, targets = load(2)
print(score(grid, cannons, targets))

meteors = []
for line in read_input(3):
    ns = nums(line)
    meteors.append((ns[0] + 1, ns[1] + 1))

targets = []
for m in meteors:
    ts = []
    t = 0
    mx, my = m
    while mx > 2 and my > 1:
        t += 1
        mx -= 1
        my -= 1
        ts.append(((mx, my), t))
    targets.append(ts)

total = 0
for ts in targets:
    best_rank = math.inf
    altitude = 1
    for (tx, ty), t1 in ts:
        for cx, cy in cannons:
            good, power, t2 = can_hit((cx, cy), (tx, ty))
            if good and ty >= altitude and t1 >= t2:
                rank = (ord(grid[len(grid) - cy - 1][cx]) - 64) * power
                if ty > altitude:
                    altitude = ty
                    best_rank = rank
                else:
                    best_rank = min(best_rank, rank)
    total += best_rank
print(total)
