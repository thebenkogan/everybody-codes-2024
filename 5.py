from collections import defaultdict
from ec import read_input


def read_cols(p):
    lines = read_input(p)
    rows = [[int(n) for n in line.split()] for line in lines]
    cols = [[row[i] for row in rows] for i in range(len(rows[0]))]
    return cols


def do_round(rnd, cols):
    N = len(cols)
    rnd = rnd % N
    clapper = cols[rnd][0]
    cols[rnd] = cols[rnd][1:]
    nxt = cols[(rnd + 1) % N]

    pos = (clapper - 1) % (2 * len(nxt))
    if pos >= len(nxt):
        pos = 2 * len(nxt) - pos
    nxt.insert(pos, clapper)


cols = read_cols(1)
for round in range(10):
    do_round(round, cols)

print("".join([str(col[0]) for col in cols]))

cols = read_cols(2)
times = defaultdict(int)
round = 0
while True:
    do_round(round, cols)
    key = "".join([str(col[0]) for col in cols])
    times[key] += 1
    if times[key] == 2024:
        print(int(key) * (round + 1))
        break
    round += 1

cols = read_cols(3)
round = 0
best = 0
while True:
    do_round(round, cols)
    key = "".join([str(col[0]) for col in cols])
    key = int(key)
    if key > best:
        best = key
        print(best)
    round += 1
