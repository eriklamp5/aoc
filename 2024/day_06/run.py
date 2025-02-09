
def getStart(board: list[str]) -> tuple[int, int]:
    for x in range(len(board)):
        line = board[x]
        for dir in "^V<>":
            if line.find(dir) != -1:
                return x, line.find(dir)
    print("not found")
    return -1, -1


def isObstruction(board: list[str], x: int, y: int) -> bool:
    if x == -1 or x == len(board) or y == -1 or y == len(board[0]):
        return False
    return board[x][y] == "#"


def move(board: list[str], pos: tuple[int, int], dir: str) -> tuple[tuple[int, int], str]:
    if dir == "^":
        if isObstruction(board, pos[0]-1, pos[1]):
            return pos, ">"
        else:
            return (pos[0]-1, pos[1]), dir
    elif dir == ">":
        if isObstruction(board, pos[0], pos[1]+1):
            return pos, "V"
        else:
            return (pos[0], pos[1]+1), dir
    elif dir == "V":
        if isObstruction(board, pos[0]+1, pos[1]):
            return pos, "<"
        else:
            return (pos[0]+1, pos[1]), dir
    elif dir == "<":
        if isObstruction(board, pos[0], pos[1]-1):
            return pos, "^"
        else:
            return (pos[0], pos[1]-1), dir
    else:
        print("fail", pos, dir)
        return (-1, -1), dir


def partOne(board: list[str]):

    pos = getStart(board)
    dir = board[pos[0]][pos[1]]
    maxX = len(board)
    maxY = len(board[0])
    encountered = [[0] * maxY for _ in range(maxX)]
    print(maxX, maxY, dir)
    while pos[0] > 0 and pos[1] > 0 and pos[0] < maxX and pos[1] < maxY:
        encountered[pos[0]][pos[1]] = 1
        pos, dir = move(board, pos, dir)
        # print(pos, dir)

    for e in encountered:
        print(e)
    # print(encountered)
    print(sum([sum(x) for x in encountered]))


def partTwo(board: list[str]):
    pass


filename = "2024/day_06/input.txt"
# filename = "2024/day_06/example.txt"
# filename = "2024/day_06/example2.txt"
with open(filename) as file:
    board = [l.strip() for l in file.readlines()]

    print(getStart(board))

    partOne(board)
    # partTwo(board)
