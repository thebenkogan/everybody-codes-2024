from collections import deque
import math
from ec import nums, read_input


lines = read_input(1, split_lines=False)
moves = lines.split(",")

highest = 0
y = 0
for move in moves:
    n = nums(move)[0]
    if move[0] == "U":
        y += n
    elif move[0] == "D":
        y -= n
    highest = max(highest, y)

print(highest)


def create_tree(p):
    lines = read_input(p)
    pos = set()
    leaves = set()
    for plant in lines:
        moves = plant.split(",")
        x, y, z = 0, 0, 0
        for move in moves:
            n = nums(move)[0]
            match move[0]:
                case "U":
                    dx, dy, dz = 0, 0, 1
                case "D":
                    dx, dy, dz = 0, 0, -1
                case "L":
                    dx, dy, dz = -1, 0, 0
                case "R":
                    dx, dy, dz = 1, 0, 0
                case "F":
                    dx, dy, dz = 0, 1, 0
                case "B":
                    dx, dy, dz = 0, -1, 0
            for _ in range(n):
                x, y, z = x + dx, y + dy, z + dz
                pos.add((x, y, z))
        leaves.add((x, y, z))
    return pos, leaves


pos, _ = create_tree(2)
print(len(pos))


dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]


def bfs(start, leaves, segments):
    q = deque([(start, 0)])
    seen = set()
    total = 0
    while len(q) > 0:
        p, steps = q.popleft()
        if p in leaves:
            total += steps

        x, y, z = p
        for dx, dy, dz in dirs:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) in seen or (nx, ny, nz) not in segments:
                continue
            seen.add((nx, ny, nz))
            q.append(((nx, ny, nz), steps + 1))

    return total


pos, leaves = create_tree(3)
max_z = max(leaves, key=lambda p: p[2])[2]
best = math.inf
l, r = 0, max_z
while True:
    mid = (l + r) // 2
    low = bfs((0, 0, mid - 1), leaves, pos)
    curr = bfs((0, 0, mid), leaves, pos)
    high = bfs((0, 0, mid + 1), leaves, pos)
    if curr <= low and curr <= high:
        print(curr)
        exit()
    elif curr < high:
        r = mid
    else:
        l = mid
