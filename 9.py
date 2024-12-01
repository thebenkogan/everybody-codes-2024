from math import inf
from ec import read_input


def count_beetles(brightness, stamps):
    DP = [0] * (brightness + 1)
    DP[1] = 1
    for b in range(2, brightness + 1):
        best = inf
        for s in stamps:
            if b - s >= 0:
                best = min(best, DP[b - s] + 1)
        DP[b] = best
    return DP


bs = [int(n) for n in read_input(1)]
stamps = [1, 3, 5, 10]
totals = [count_beetles(b, stamps)[-1] for b in bs]
print(sum(totals))

bs = [int(n) for n in read_input(2)]
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
totals = [count_beetles(b, stamps)[-1] for b in bs]
print(sum(totals))

bs = [int(n) for n in read_input(3)]
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
total = 0
for b in bs:
    end = b // 2
    start = end - 49
    DP = count_beetles(end + 51, stamps)
    best = inf
    for i in range(start, end + 1):
        l, r = DP[i], DP[b - i]
        best = min(best, l + r)
    total += best

print(total)
