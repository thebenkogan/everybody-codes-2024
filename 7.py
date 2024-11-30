from itertools import permutations
from ec import DIRS, read_input


def apply_action(val, action):
    match action:
        case "+":
            val += 1
        case "-":
            val = max(val - 1, 0)
    return val


# part 1

lines = read_input(1)
plans = {}
for line in lines:
    a, b = line.split(":")
    b = b.split(",")
    plans[a] = b

ranks = {}
for key, track in plans.items():
    val = 10
    total = 10
    for t in track:
        val = apply_action(val, t)
        total += val
    ranks[key] = total

s = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
print("".join([k for k, _ in s]))

# part 2

sections = read_input(2, split_lines=False)
lines, track = sections.split("\n\n")
track = track.splitlines()
plans = {}
for line in lines.splitlines():
    a, b = line.split(":")
    b = b.split(",")
    plans[a] = b

ranks = {}
for key, plan in plans.items():
    val = 10
    total = 0
    loops = 0
    pos = 0
    x, y = 1, 0
    dx, dy = 1, 0
    while loops < 10:
        track_action = track[y][x]
        action = plan[pos % len(plan)]
        if track_action == "-" or track_action == "+":
            action = track_action
        val = apply_action(val, action)
        total += val
        pos += 1
        if track_action == "S":
            loops += 1
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(track[0]) or ny < 0 or ny >= len(track):
            dx, dy = -dy, dx
            nx, ny = x + dx, y + dy
        x, y = nx, ny
    ranks[key] = total


s = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
print("".join([k for k, _ in s]))

# part 3

sections = read_input(3, split_lines=False)
plan, track = sections.split("\n\n")
track = track.splitlines()
plan = plan.split(":")[1].split(",")

flat_track = []
curr = (0, 0)
prev = (0, 1)
while True:
    for dx, dy in DIRS:
        nx, ny = curr[0] + dx, curr[1] + dy
        if (nx, ny) == prev:
            continue
        if ny < 0 or ny >= len(track) or nx < 0 or nx >= len(track[ny]):
            continue
        if track[ny][nx] == " ":
            continue
        action = track[ny][nx]
        break
    flat_track.append(action)
    prev = curr
    curr = (nx, ny)
    if action == "S":
        break


# every 11 loops, it restarts, so we just run 11 times then multiply by 2024/11 = 184
def grade(plan, flat_track):
    total = 0
    val = 10
    pos = 0
    for track_pos in range(len(flat_track) * 11):
        action = plan[pos % len(plan)]
        track_action = flat_track[track_pos % len(flat_track)]
        if track_action == "-" or track_action == "+":
            action = track_action
        val = apply_action(val, action)
        total += val
        pos += 1
    return total * 184


target = grade(plan, flat_track)
total = 0
opts = ["+", "+", "+", "+", "+", "-", "-", "-", "=", "=", "="]
plans = set()
for opt in permutations(opts):
    plans.add("".join(opt))
plans = [[c for c in p] for p in plans]

for i, opt in enumerate(plans):
    g = grade(opt, flat_track)
    if g > target:
        total += 1

print(total)
