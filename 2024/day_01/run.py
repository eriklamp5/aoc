




def partOne(left: list[int], right: list[int]):
    left = sorted(left)
    right = sorted(right)
    both = [x for x in zip(left, right)]
    sums = sum([abs(x[0] - x[1]) for x in both])
    # print(left)
    # print(right)
    # print(both)
    print(sums)


def partTwo(left: list[int], right: list[int]):
    rightCounts = {}
    for i in right:
        if i not in rightCounts:
            rightCounts[i] = 0
        rightCounts[i] += 1
    sums = sum([x * rightCounts.get(x, 0) for x in left])
    # print(left)
    # print(right)
    # print(rightCounts)
    print(sums)


filename = "2024/day_01/input.txt"
# filename = "2024/day_01/example.txt"
with open(filename) as file:
    left, right = zip(*[line.split("   ") for line in file])
    left = [int(x.strip()) for x in left]
    right = [int(x.strip()) for x in right]
    # partOne(left, right)
    partTwo(left, right)

