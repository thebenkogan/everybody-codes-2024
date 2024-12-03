from math import inf
from ec import read_input


def read_conversions(p):
    lines = read_input(p)
    adj = {}
    for line in lines:
        a, b = line.split(":")
        adj[a] = b.split(",")
    return adj


def grow(adj, p, n):
    DP = {k: [0] * (n + 1) for k in adj.keys()}
    for k, v in DP.items():
        v[1] = len(adj[k])

    for d in range(2, n + 1):
        for k, v in DP.items():
            v[d] = sum(DP[c][d - 1] for c in adj[k])

    return DP[p][-1]


adj = read_conversions(1)
print(grow(adj, "A", 4))

adj = read_conversions(2)
print(grow(adj, "Z", 10))

adj = read_conversions(3)
low = inf
high = 0
for k in adj.keys():
    size = grow(adj, k, 20)
    low = min(low, size)
    high = max(high, size)
print(high - low)
