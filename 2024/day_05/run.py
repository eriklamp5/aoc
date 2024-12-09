

def passes(ord: dict[int, list[int]], line: list[int]) -> bool:
    banned = set()
    for i in line:
        if i in banned:
            return False
        if i in ord:
            banned.update(ord[i])
    return True


def partOne(ord: dict[int, list[int]], lines: list[list[int]]):
    mids = [l[len(l)//2] for l in lines if passes(ord, l)]
    print(mids)
    print(sum(mids))


def improve(ord: dict[int, list[int]], line: list[int]) -> list[int]:
    seen = set()
    banned = {}
    for i in line:
        if i in banned:
            reasons = banned[i]
            indexes = [line.index(r) for r in reasons]
            newIdx = min(indexes)
            del line[line.index(i)]
            line.insert(newIdx, i)
            return line
        if i in ord:
            for b in ord[i]:
                if b not in banned:
                    banned[b] = []
                banned[b].append(i)
    raise "stuck"


def partTwo(ord: dict[int, list[int]], lines: list[list[int]]):
    unfixed = [l for l in lines if not passes(ord, l)]
    print(unfixed)
    mids = []
    for line in unfixed:
        while not passes(ord, line):
            # print(line)
            line = improve(ord, line)
        mids.append(line[len(line)//2])
    print(mids)
    print(sum(mids))


filename = "2024/day_05/input.txt"
# filename = "2024/day_05/example.txt"
# filename = "2024/day_05/example2.txt"
with open(filename) as file:
    orderings = {}
    while True:
        line = file.readline().strip()
        if line == "":
            break
        split = line.split("|")
        pivot = int(split[1])
        after = int(split[0])
        if pivot not in orderings:
            orderings[pivot] = []
        orderings[pivot].append(after)

    lines = [[int(y) for y in x.strip().split(",")] for x in file.readlines()]
    print(orderings)
    print(lines)

    # partOne(orderings, lines)
    partTwo(orderings, lines)
