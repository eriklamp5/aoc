import re

counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse(baseline):
    split = baseline.split(":")
    gameval = int(split[0].split(" ")[1])
    print(f"{gameval}: {baseline}")

    for pulls in split[1].split(";"):
        spulls = pulls.split(",")
        for pull in spulls:
            spull = pull.strip().split(" ")
            count = int(spull[0])
            color = spull[1]
            # print(f"{count}x{color}")
            if count > counts[color]:
                return 0

    return gameval


def parse_min(baseline):
    split = baseline.split(":")
    gameval = int(split[0].split(" ")[1])
    print(f"{gameval}: {baseline}")
    mins = {
    "red": 0,
    "green": 0,
    "blue": 0,
    }

    for pulls in split[1].split(";"):
        spulls = pulls.split(",")
        for pull in spulls:
            spull = pull.strip().split(" ")
            count = int(spull[0])
            color = spull[1]
            # print(f"{count}x{color}")
            if count > mins[color]:
                mins[color] = count

    return mins["red"] * mins["green"] * mins["blue"]

filename = "day_02/input.txt"
# filename = "day_02/example.txt"
with open(filename) as file:
    total = sum([parse_min(line.strip()) for line in file])
    print(total)

