from ec import read_input

cost = {
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}

p1 = read_input(1, split_lines=False)
total = sum([cost[c] for c in p1])
print(total)

p2 = read_input(2, split_lines=False)
total = 0
for i in range(0, len(p2), 2):
    a, b = p2[i], p2[i + 1]
    c1 = cost[a] if a in cost else 0
    c2 = cost[b] if b in cost else 0
    total += c1 + c2
    if a in cost and b in cost:
        total += 2

print(total)

p3 = read_input(3, split_lines=False)
total = 0
for i in range(0, len(p3), 3):
    a, b, c = p3[i], p3[i + 1], p3[i + 2]
    c1 = cost[a] if a in cost else 0
    c2 = cost[b] if b in cost else 0
    c3 = cost[c] if c in cost else 0
    total += c1 + c2 + c3
    num = 0
    for c in [a, b, c]:
        if c in cost:
            num += 1
    total += (num - 1) * num

print(total)
