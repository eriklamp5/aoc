import re


pattern = re.compile("mul\\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\\)")

pattern2 = re.compile(r"(do)\(\)|(don't)\(\)|(mul)\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)")

def partOne(line: str):
    print(line)
    matches = pattern.findall(line)
    print(matches)
    sums = sum([ int(x[0]) * int(x[1]) for x in matches])
    print(sums)

def partTwo(line: str):
    print(line)
    matches = pattern2.findall(line)
    print(matches)
    sum = 0
    enabled = True
    for m in matches:
        if m[2] == "mul":
            if not enabled:
                continue
            sum += int(m[3]) * int(m[4])
        elif m[0] == "do":
            enabled = True
        elif m[1] == "don't":
            enabled = False
    print(sum)


filename = "2024/day_03/input.txt"
# filename = "2024/day_03/example.txt"
# filename = "2024/day_03/example2.txt"
with open(filename) as file:
    line = file.read()
    # partOne(line)
    partTwo(line)

