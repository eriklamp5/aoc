



def dist(time, duration):
    return time * (duration - time)

def run_dist(race):
    lower = None
    upper = None
    for i in range(1, race[0]):
        if dist(i, race[0]) > race[1]:
            if lower is None:
                lower = i
            upper = i
        if dist(i, race[0]) < race[1] and upper != None:
            return lower, upper

def run_dist_two(race):
    for i in range(1, race[0]):
        if dist(i, race[0]) > race[1]:
            return i, race[0] - i



def part_one():
    with open(filename) as file:
        
        time = map(int, [x for x in file.readline().strip().split(" ") if x != ""][1:])
        distance = map(int, [x for x in file.readline().strip().split(" ") if x != ""][1:])
        races = [x for x in zip(time, distance)]

        print(races)
        dists = [run_dist(x) for x in races]
        print(dists)
        total = 1
        for d in dists:
            total = total * (d[1] - d[0] + 1)
        print(total)


def part_two():
    with open(filename) as file:
        
        time = int(file.readline().strip().split(":")[1].replace(" ", ""))
        distance = int(file.readline().strip().split(":")[1].replace(" ", ""))
        print(f"{time} {distance}")
        parsed = run_dist_two((time, distance))
        print(parsed)
        print(parsed[1] - parsed[0] + 1)



filename = "day_06/input.txt"
# filename = "day_06/example.txt"
# part_one()
part_two()



