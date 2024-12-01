from collections import defaultdict
from ec import read_input

n = read_input(1, split_lines=False)
n = int(n)

width = 1
while n > 0:
    n -= width
    width += 2

print((width - 2) * abs(n))

n = read_input(2, split_lines=False)
n = int(n)
mod = 1111
available = 20240000
thickness = 1
width = 1
available -= thickness
while available > 0:
    thickness = (thickness * n) % mod
    width += 2
    available -= thickness * width

print(abs(available) * width)


def blocks_needed(n, layers):
    mod = 10
    thickness = 1
    width = 1
    pos = 0
    cols = defaultdict(int)
    cols[0] = 1
    for _ in range(layers - 1):
        thickness = (thickness * n) % mod + mod
        pos += 1
        width += 2
        for i in range(-pos, pos + 1):
            cols[i] += thickness

    total = sum(cols.values())
    for p, col in cols.items():
        if abs(p) == pos:
            continue
        remove = (width * n * col) % mod
        total -= remove

    return total


n = read_input(3, split_lines=False)
n = int(n)
available = 202400000

l, r = 1, 5000
while l < r:
    mid = (l + r) // 2
    bd = blocks_needed(n, mid)
    if bd < available:
        l = mid + 1
    elif bd > available:
        r = mid - 1

print(blocks_needed(n, r) - available)
