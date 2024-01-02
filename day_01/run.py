import re

def map(line):
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    return line

def parse(baseline, debug = False):
    # line = line.replace("zero", "0")
    vals = re.findall("(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", baseline)
    value = int(map(vals[0])) * 10 + int(map(vals[-1]))
    if debug:
        print(baseline + " " + str(value))
    return value

parse("twone", debug=True)

filename = "day_01/input.txt"
# filename = "day_01/example.txt"
with open(filename) as file:
    total = sum([parse(line.rstrip()) for line in file])
    print(total)

