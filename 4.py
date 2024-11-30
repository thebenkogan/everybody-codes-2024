from statistics import median
from ec import read_input


def align(p):
    lines = read_input(p)
    ns = [int(n) for n in lines]

    shortest = min(ns)
    return sum([n - shortest for n in ns])


print(align(1))
print(align(2))

p3 = read_input(3)
ns = [int(n) for n in p3]
med = int(median(ns))
print(sum([abs(n - med) for n in ns]))
