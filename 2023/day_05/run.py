
def convert_map_line(line):
    line = line.split(" ")
    dest = int(line[0].strip())
    src = int(line[1].strip())
    leng = int(line[2].strip())
    return (src, leng, dest - src)

def expect_line(line, expected):
    if line != expected:
        print(f"line '{line}'")

def apply_mapping(source, maplist):
    for bind in maplist:
        if bind[0] <= source and source < bind[0] + bind[1]:
            return source + bind[2]
    return source

def ranges_overlap(source, mapping):
    overlapping = []
    nonoverlap = []
    # print(f"{source} {mapping}")
    if source[0] + source[1] <= mapping[0]:
        # source is entirely less than mapping
        return [], [source]
    if mapping[0] + mapping[1] <= source[0]:
        # mapping is entirely less than source
        return [], [source]
    if source[0] < mapping[0]:
        nonoverlap.append((source[0], mapping[0] - source[0]))
        remainder = source[0] + source[1] - mapping[0]
        if remainder < mapping[1]:
            overlapping.append((mapping[0], remainder))
            return overlapping, nonoverlap
        overlapping.append((mapping[0], mapping[1]))
        nonoverlap.append((mapping[0] + mapping[1], remainder - mapping[1]))
        return overlapping, nonoverlap
    remainder = mapping[0] + mapping[1] - source[0]
    if remainder < source[1]:
        overlapping.append((source[0], remainder))
        nonoverlap.append((source[0] + remainder, source[1] - remainder))
        return overlapping, nonoverlap
    overlapping.append((source[0], source[1]))
    return overlapping, nonoverlap

def apply_mapping_range(sources, maplist):
    new_ranges = []
    while len(sources) != 0:
        source = sources.pop()
        for mapping in maplist:
            over, nonover = ranges_overlap(source, mapping)
            # print(f"{source} {mapping} {over} {nonover}")
            if len(over) == 0:
                continue
            # add offset to the overlapping section
            new_ranges.extend([(x + mapping[2], y) for (x,y) in over])
            sources.extend(nonover)
            break
        else:
            # no mapping overlapps, using identity
            new_ranges.append(source)
    return new_ranges


debug = True
debug = False
filename = "day_05/input.txt"
# filename = "day_05/example.txt"
seeds = []
seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_loc = []

with open(filename) as file:
    seedline = file.readline()
    seeds = [int(x) for x in seedline.split(":")[1].strip().split(" ")]
    if debug: print(seeds)

    line = file.readline().strip()
    expect_line(line, "")

    line = file.readline().strip()
    expect_line(line, "seed-to-soil map:")
    
    line = file.readline().strip()
    while line != "":
        seed_to_soil.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(seed_to_soil)

    line = file.readline().strip()
    expect_line(line, "soil-to-fertilizer map:")
    
    line = file.readline().strip()
    while line != "":
        soil_to_fert.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(soil_to_fert)

    line = file.readline().strip()
    expect_line(line, "fertilizer-to-water map:")
    
    line = file.readline().strip()
    while line != "":
        fert_to_water.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(fert_to_water)

    line = file.readline().strip()
    expect_line(line, "water-to-light map:")
    
    line = file.readline().strip()
    while line != "":
        water_to_light.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(water_to_light)

    line = file.readline().strip()
    expect_line(line, "light-to-temperature map:")
    
    line = file.readline().strip()
    while line != "":
        light_to_temp.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(light_to_temp)

    line = file.readline().strip()
    expect_line(line, "temperature-to-humidity map:")
    
    line = file.readline().strip()
    while line != "":
        temp_to_humid.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(temp_to_humid)

    line = file.readline().strip()
    expect_line(line, "humidity-to-location map:")
    
    line = file.readline().strip()
    while line != "":
        humid_to_loc.append(convert_map_line(line))
        line = file.readline().strip()
    
    if debug: print(humid_to_loc)

def part_one():
    min_location = None
    for id in seeds:
        id = apply_mapping(id, seed_to_soil)
        id = apply_mapping(id, soil_to_fert)
        id = apply_mapping(id, fert_to_water)
        id = apply_mapping(id, water_to_light)
        id = apply_mapping(id, light_to_temp)
        id = apply_mapping(id, temp_to_humid)
        id = apply_mapping(id, humid_to_loc)
        if min_location == None or id < min_location:
            min_location = id

    print(min_location)

def part_two():
    global seeds
    seeds = [x for x in zip(seeds[::2], seeds[1::2])]
    print(seeds)

    soil = apply_mapping_range(seeds, seed_to_soil)
    print(soil)

    fert = apply_mapping_range(soil, soil_to_fert)
    print(fert)

    water = apply_mapping_range(fert, fert_to_water)
    print(water)

    light = apply_mapping_range(water, water_to_light)
    print(light)

    temp = apply_mapping_range(light, light_to_temp)
    print(temp)

    humid = apply_mapping_range(temp, temp_to_humid)
    print(humid)

    loc = apply_mapping_range(humid, humid_to_loc)
    print(loc)

    print(min([x for x,y in loc]))


# part_one()

part_two()

