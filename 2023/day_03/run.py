import re

def build_numbers(numbers, x, y):
    if x < 0 or x >= len(board):
        return
    if y < 0 or y >= len(board[0]):
        return
    if board[x][y] not in digits:
        return
    yl = y
    yr = y
    while True:
        yl -= 1
        if yl < 0 or board[x][yl] not in digits:
            yl += 1
            break
    while True:
        yr += 1
        if yr >= len(board[0]) or board[x][yr] not in digits:
            # yr -= 1
            break
    location = (x, yl, yr)
    if location not in numbers:
        numbers.append(location)

def build_permute(numbers, x, y):
    build_numbers(numbers, x-1, y-1)
    build_numbers(numbers, x, y-1)
    build_numbers(numbers, x+1, y-1)
    build_numbers(numbers, x-1, y)
    build_numbers(numbers, x+1, y)
    build_numbers(numbers, x-1, y+1)
    build_numbers(numbers, x, y+1)
    build_numbers(numbers, x+1, y+1)

def part_one():
    symbols = []
    for x in range(len(board)):
        for m in re.finditer("[^0-9.]", board[x]):
            symbols.append((x, m.start(0)))

    numbers = []
    for x, y in symbols:
        build_permute(numbers, x, y)
    # print(numbers)

    total = 0
    for x, y, z in numbers:
        total += int(board[x][y:z])

    print(total)


def part_two():
    symbols = []
    for x in range(len(board)):
        for m in re.finditer("\*", board[x]):
            symbols.append((x, m.start(0)))

    total = 0
    for x, y in symbols:
        numbers = []
        build_permute(numbers, x, y)
        # print(numbers)
        if len(numbers) == 2:
            total += int(board[numbers[0][0]][numbers[0][1]:numbers[0][2]]) * int(board[numbers[1][0]][numbers[1][1]:numbers[1][2]])

    print(total)

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
board = []

filename = "day_03/input.txt"
# filename = "day_03/example.txt"
with open(filename) as file:
    board = [line.strip() for line in file]

# print(board)
# part_one()
part_two()

