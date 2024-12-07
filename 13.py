from collections import deque
import heapq
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


def dijkstra(grid, start, end):
    sx, sy = start
    q = [(0, sx, sy)]
    seen = set()
    while len(q) > 0:
        steps, x, y = heapq.heappop(q)
        if (x, y) in end:
            return steps
        if (x, y) in seen:
            continue
        seen.add((x, y))
        level = grid[y][x]

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
                continue
            nb = grid[ny][nx]
            if nb == "#":
                continue

            hi, lo = max(level, nb), min(level, nb)
            dist = min(hi - lo, (lo + 10) - hi) + 1
            heapq.heappush(q, (steps + dist, nx, ny))


grid, starts, end = read_grid(1)
print(dijkstra(grid, starts[0], set([end])))

grid, starts, end = read_grid(2)
print(dijkstra(grid, starts[0], set([end])))

grid, starts, end = read_grid(3)
print(dijkstra(grid, end, set(starts)))
