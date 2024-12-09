

def count(grid: list[str], x: int, y: int, xlen: int, ylen: int) -> int:
    if grid[x][y] != "X":
        return 0
    total = 0
    letter = "MAS"
    if x + 3 < xlen:
        if grid[x+1][y] == letter[0] and grid[x+2][y] == letter[1] and grid[x+3][y] == letter[2]:
            total += 1
    if x - 3 >= 0:
        if grid[x-1][y] == letter[0] and grid[x-2][y] == letter[1] and grid[x-3][y] == letter[2]:
            total += 1
    if y + 3 < ylen:
        if grid[x][y+1] == letter[0] and grid[x][y+2] == letter[1] and grid[x][y+3] == letter[2]:
            total += 1
    if y - 3 >= 0:
        if grid[x][y-1] == letter[0] and grid[x][y-2] == letter[1] and grid[x][y-3] == letter[2]:
            total += 1

    if x + 3 < xlen and y + 3 < ylen:
        if grid[x+1][y+1] == letter[0] and grid[x+2][y+2] == letter[1] and grid[x+3][y+3] == letter[2]:
            total += 1
    if x + 3 < xlen and y - 3 >= 0:
        if grid[x+1][y-1] == letter[0] and grid[x+2][y-2] == letter[1] and grid[x+3][y-3] == letter[2]:
            total += 1
    if x - 3 >= 0 and y + 3 < ylen:
        if grid[x-1][y+1] == letter[0] and grid[x-2][y+2] == letter[1] and grid[x-3][y+3] == letter[2]:
            total += 1
    if x - 3 >= 0 and y - 3 >= 0:
        if grid[x-1][y-1] == letter[0] and grid[x-2][y-2] == letter[1] and grid[x-3][y-3] == letter[2]:
            total += 1

    return total


def partOne(grid: list[str]):
    xlen = len(grid)
    ylen = len(grid[0])
    sums = sum([sum([count(grid, x, y, xlen, ylen) for y in range(ylen)])
               for x in range(xlen)])
    print(sums)


def countGrid(grid: list[str], x: int, y: int, xlen: int, ylen: int) -> int:
    if grid[x][y] != "A":
        return 0
    if x == 0 or x == xlen - 1:
        return 0
    if y == 0 or y == ylen - 1:
        return 0

    mCount = 0
    sCount = 0
    if grid[x-1][y-1] == "M":
        mCount += 1
    if grid[x-1][y-1] == "S":
        sCount += 1
    if grid[x-1][y+1] == "M":
        mCount += 1
    if grid[x-1][y+1] == "S":
        sCount += 1
    if grid[x+1][y-1] == "M":
        mCount += 1
    if grid[x+1][y-1] == "S":
        sCount += 1
    if grid[x+1][y+1] == "M":
        mCount += 1
    if grid[x+1][y+1] == "S":
        sCount += 1

    if mCount == 2 and sCount == 2 and grid[x-1][y-1] != grid[x+1][y+1]:
        return 1
    return 0


def partTwo(grid: list[str]):
    xlen = len(grid)
    ylen = len(grid[0])
    sums = sum([sum([countGrid(grid, x, y, xlen, ylen) for y in range(ylen)])
               for x in range(xlen)])
    print(sums)


filename = "2024/day_04/input.txt"
# filename = "2024/day_04/example.txt"
# filename = "2024/day_04/example2.txt"
with open(filename) as file:
    lines = [x.strip() for x in file.readlines()]
    print(lines)
    # partOne(lines)
    partTwo(lines)
