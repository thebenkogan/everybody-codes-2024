from collections import defaultdict, deque
from ec import read_input


def get_unique_path(p):
    lines = read_input(p)

    adj = {}
    for line in lines:
        a, b = line.split(":")
        b = b.split(",")
        adj[a] = b

    start = "RR"
    q = deque([(start, [start])])
    seen = set([start])
    paths = defaultdict(list)
    while len(q) > 0:
        elt, path = q.popleft()
        if elt == "@":
            paths[len(path)].append(path)
        if elt not in adj:
            continue
        for n in adj[elt]:
            if n not in seen:
                new_path = path + [n]
                q.append((n, new_path))
                if n != "@":
                    seen.add(n)

    for ps in paths.values():
        if len(ps) == 1:
            return ps[0]


p1 = get_unique_path(1)
print("".join(p1))

p2 = get_unique_path(2)
print("".join([l[0] for l in p2]))

p3 = get_unique_path(3)
print("".join([l[0] for l in p3]))
