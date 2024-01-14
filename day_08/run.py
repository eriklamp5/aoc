import re


nodes = {}

def add_node(line):
    if line == "":
        return
    line = line.replace(" ", "").replace("(", "").replace(")", "")
    split = re.split('=|,', line)
    src = split[0]
    left = split[1]
    right = split[2]
    # print(f"{src} -> {left}, {right}")
    nodes[src] = (left, right)

def traverse(base_instr):
    steps = 0
    cur_node = "AAA"
    remain_instr = base_instr
    while True:
        if remain_instr == "":
            remain_instr = base_instr
        if cur_node == "ZZZ":
            return steps
        instr = remain_instr[0]
        remain_instr = remain_instr[1:]
        steps += 1
        if instr == "L":
            cur_node = nodes[cur_node][0]
        if instr == "R":
            cur_node = nodes[cur_node][1]

def traverse_parallel(base_instr):
    steps = 0
    cur_nodes = [x for x in nodes.keys() if x.endswith("A")]
    print(cur_nodes)
    remain_instr = base_instr
    while True:
        if remain_instr == "":
            remain_instr = base_instr
        if all([x.endswith("Z") for x in cur_nodes]):
            return steps
        instr = remain_instr[0]
        remain_instr = remain_instr[1:]
        steps += 1
        if instr == "L":
            cur_nodes = [nodes[x][0] for x in cur_nodes]
        if instr == "R":
            cur_nodes = [nodes[x][1] for x in cur_nodes]

filename = "day_08/input.txt"
# filename = "day_08/example3.txt"
# filename = "day_08/example2.txt"
# filename = "day_08/example.txt"
with open(filename) as file:
    instr = file.readline().strip()
    # print(instr)
    for line in file:
        add_node(line.strip())
    # print(nodes)
    # print(traverse(instr))
    print(traverse_parallel(instr))



