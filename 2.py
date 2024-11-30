from ec import read_input, DIRS
import re


def parse_input(p):
    p = read_input(p, split_lines=False)
    sections = p.split("\n\n")
    words, sentence = sections[0], sections[1]
    words = words.split(":")[1].split(",")
    return words, sentence


words, sentence = parse_input(1)
total = 0
for w in words:
    total += len(re.findall(w, sentence))

print(total)

words, sentence = parse_input(2)
lines = sentence.splitlines()


total = 0
for line in lines:
    syms = set()
    for w in words:
        wreg = re.compile(f"(?={w}|{w[::-1]})")
        for m in wreg.finditer(line):
            span = m.span()
            for i in range(span[0], span[0] + len(w)):
                syms.add(i)
    total += len(syms)

print(total)

words, sentence = parse_input(3)
lines = sentence.splitlines()

seen = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        for w in words:
            if w[0] != c:
                continue
            for dx, dy in DIRS:
                positions = [(x, y)]
                nx, ny = x, y
                for i in range(1, len(w)):
                    nx = (nx + dx) % len(line)
                    ny += dy
                    if ny < 0 or ny >= len(lines):
                        break
                    if lines[ny][nx] == w[i]:
                        positions.append((nx, ny))
                    else:
                        break
                if len(positions) == len(w):
                    seen.update(positions)

print(len(seen))
