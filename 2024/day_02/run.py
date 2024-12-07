


def safe(report: list[int]) -> bool:
    print(report)
    if report[0] < report[1]:
        last = report[0] - 1
        for i in report:
            diff = i - last
            last = i
            if  diff > 3 or diff < 1:
                return False
        return True
    elif report[0] > report[1]:
        last = report[0] + 1
        for i in report:
            diff = last - i
            last = i
            if  diff > 3 or diff < 1:
                return False
        return True
    else:
        return False

def partOne(reports: list[list[int]]):
    sums = sum([1 if safe(x) else 0 for x in reports])
    # print(reports)
    print(sums)

def safeTwo(report: list[int]) -> bool:
    print(report)
    if safe(report):
        return True
    for i in range(len(report)):
        if safe(report[:i] + report[i+1:]):
            return True
    return False

def partTwo(reports: list[list[int]]):
    sums = sum([1 if safeTwo(x) else 0 for x in reports])
    # print(reports)
    print(sums)


filename = "2024/day_02/input.txt"
# filename = "2024/day_02/example.txt"
with open(filename) as file:
    reports = [[int(x.strip()) for x in line.split(" ")] for line in file]
    # partOne(reports)
    partTwo(reports)

