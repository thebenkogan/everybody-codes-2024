from collections import defaultdict, deque
import heapq
from ec import DIRS, read_input


def read_grid(p):
    lines = read_input(p)
    grid = [[c for c in line] for line in lines]

    for i, c in enumerate(grid[0]):
        if c == ".":
            sx, sy = i, 0
            grid[0][i] = "S"

    return grid, sx, sy


def bfs(grid, x, y):
    t = grid[y][x]
    q = deque([(x, y, 0, set())])
    seen = {(x, y)}
    dists = defaultdict(list)
    while len(q) > 0:
        cx, cy, steps, seen_plants = q.popleft()
        c = grid[cy][cx]
        if c not in {"#", ".", "~"}:
            sp = seen_plants.copy()
            sp.add(c)
            dists[c].append((cx, cy, steps, sp))

        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid[0])
                or ny >= len(grid)
                or (nx, ny) in seen
                or grid[ny][nx] in {"#", "~"}
            ):
                continue

            new_seen_plants = seen_plants
            if c not in {"#", ".", "~", "S", t}:
                new_seen_plants = seen_plants.copy()
                new_seen_plants.add(c)

            seen.add((nx, ny))
            q.append((nx, ny, steps + 1, new_seen_plants))

    return dists


grid, sx, sy = read_grid(1)
dists = bfs(grid, sx, sy)
print(min(dists["H"], key=lambda c: c[2])[2] * 2)


def tsm(grid, sx, sy):
    adj = {}
    plants = set()
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c in {"#", ".", "~"}:
                continue
            plants.add(c)
            dists = bfs(grid, x, y)
            adj[(x, y)] = dists

    q = [(0, sx, sy, set())]
    seen = set()
    while len(q) > 0:
        steps, x, y, seen_plants = heapq.heappop(q)
        key = (x, y, str(sorted(seen_plants)))
        if key in seen:
            continue
        if (x, y) != (sx, sy):
            seen.add(key)

        if (x, y) == (sx, sy) and len(seen_plants) == len(plants):
            return steps

        for plant, positions in adj[(x, y)].items():
            if plant in seen_plants:
                continue
            for nx, ny, w, ps in positions:
                new_seen_plants = seen_plants.copy()
                new_seen_plants.add(plant)
                new_seen_plants.update(ps)
                if (nx, ny) == (sx, sy) and len(new_seen_plants) != len(plants):
                    continue
                heapq.heappush(q, (steps + w, nx, ny, new_seen_plants))


grid, sx, sy = read_grid(2)
print(tsm(grid, sx, sy))

grid, _, _ = read_grid(3)
width = len(grid[0]) // 3
left = [line[:width] for line in grid]
middle = [line[width : 2 * width] for line in grid]
right = [line[2 * width :] for line in grid]

# replace other K with unique letter, then run TSM on middle
sx, sy = middle[0].index("S"), 0
dists = bfs(middle, sx, sy)
left_k, right_k = dists["K"]
middle[left_k[1]][left_k[0]] = "Z"
middle_cost = tsm(middle, sx, sy)

for y, line in enumerate(left):
    for x, c in enumerate(line):
        if c == "E" and x > 1:
            left_cost = tsm(left, x, y)

for y, line in enumerate(right):
    for x, c in enumerate(line):
        if c == "R" and x < len(line) - 2:
            right_cost = tsm(right, x, y)

print(left_cost + right_cost + middle_cost + 12)  # +12 for connections between K's
