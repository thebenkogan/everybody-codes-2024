from collections import deque
from ec import DIRS, read_input


def read_grid(p):
    lines = read_input(p)
    grid = [[c for c in line] for line in lines]
    starts = []
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                starts.append((x, y))
            elif c == "E":
                ex, ey = x, y
            elif c.isdigit():
                grid[y][x] = int(c)
    for sx, sy in starts:
        grid[sy][sx] = 0
    grid[ey][ex] = 0

    return (grid, starts, (ex, ey))


def bfs(grid, start, end):
    sx, sy = start
    q = deque([(sx, sy, 0, 0)])
    seen = set([(sx, sy, 0)])
    while len(q) > 0:
        x, y, level, steps = q.popleft()
        if (x, y) in end:
            return steps

        # first try moving up and down
        for dy in [-1, 1]:
            new_level = (level + dy) % 10
            if (x, y, new_level) in seen:
                continue
            seen.add((x, y, new_level))
            q.append((x, y, new_level, steps + 1))

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            nb = grid[ny][nx]
            if nb == "#" or nb != level or (nx, ny, level) in seen:
                continue

            seen.add((nx, ny, level))
            q.append((nx, ny, level, steps + 1))


grid, starts, end = read_grid(1)
print(bfs(grid, starts[0], set([end])))

grid, starts, end = read_grid(2)
print(bfs(grid, starts[0], set([end])))

grid, starts, end = read_grid(3)
print(bfs(grid, end, set(starts)))
