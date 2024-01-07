from collections import Counter
from functools import cmp_to_key


five_of_kind = 7
four_of_kind = 6
full_house = 5
three_of_kind = 4
two_pair = 3
one_pair = 2
high_card = 1

def compare_card(l, r):
    if l[0] != r[0]:
        return l[0] - r[0]
    for i in range(5):
        x = l[1][i]
        y = r[1][i]
        if x == y:
            continue
        for c in "AKQJT":
            if x == c:
                return 1
            if y == c:
                return -1
        if int(x) - int(y) != 0:
            return int(x) - int(y)
    return 0

def parse_line(line):
    line = line.split(" ")
    hand_str = line[0]
    bid = int(line[1])
    hand_sorted = sorted(hand_str)
    hand_counts = Counter(hand_sorted)
    hand_counts = sorted(hand_counts.items(), key=lambda item: item[1], reverse=True)
    # print(hand_counts)
    if hand_counts[0][1] == 5:
        return (five_of_kind, hand_str, bid)
    if hand_counts[0][1] == 4:
        return (four_of_kind, hand_str, bid)
    if hand_counts[0][1] == 3 and hand_counts[1][1] == 2:
        return (full_house, hand_str, bid)
    if hand_counts[0][1] == 3:
        return (three_of_kind, hand_str, bid)
    if hand_counts[0][1] == 2 and hand_counts[1][1] == 2:
        return (two_pair, hand_str, bid)
    if hand_counts[0][1] == 2:
        return (one_pair, hand_str, bid)
    if hand_counts[0][1] == 1:
        return (high_card, hand_str, bid)
    
    print(f"unscored hand: {hand_str}")
    return (0, hand_str, bid)

def compare_card_two(l, r):
    if l[0] != r[0]:
        return l[0] - r[0]
    for i in range(5):
        x = l[1][i]
        y = r[1][i]
        if x == y:
            continue
        for c in "AKQT":
            if x == c:
                return 1
            if y == c:
                return -1
        if x == 'J':
            return -1
        if y == 'J':
            return 1
        if int(x) - int(y) != 0:
            return int(x) - int(y)
    return 0

def parse_line_two(line):
    line = line.split(" ")
    hand_str = line[0]
    bid = int(line[1])
    hand_count = sorted(hand_str)
    hand_count = Counter(hand_count)
    joker_count = hand_count['J'] if 'J' in hand_count else 0
    del hand_count['J']
    hand_counts = sorted(hand_count.items(), key=lambda item: item[1], reverse=True)
    # print(hand_counts, joker_count)

    if len(hand_counts) == 0:
        return (five_of_kind, hand_str, bid)    

    if hand_counts[0][1] == 5 - joker_count:
        return (five_of_kind, hand_str, bid)
    if hand_counts[0][1] == 4 - joker_count:
        return (four_of_kind, hand_str, bid)
    if hand_counts[0][1] == 3 - joker_count and hand_counts[1][1] == 2:
        return (full_house, hand_str, bid)
    if hand_counts[0][1] == 3 - joker_count:
        return (three_of_kind, hand_str, bid)
    if hand_counts[0][1] == 2 - joker_count and hand_counts[1][1] == 2:
        return (two_pair, hand_str, bid)
    if hand_counts[0][1] == 2 - joker_count:
        return (one_pair, hand_str, bid)
    if hand_counts[0][1] == 1:
        return (high_card, hand_str, bid)
    
    print(f"unscored hand: {hand_str}")
    return (0, hand_str, bid)


filename = "day_07/input.txt"
# filename = "day_07/example.txt"

def part_one():
    with open(filename) as file:
        lines = [parse_line(line.strip()) for line in file]
        print(lines)
        lines = sorted(lines, key=cmp_to_key(compare_card))
        print(lines)
        total = 0
        for i in range(len(lines)):
            total = total + (i + 1) * lines[i][2]
        print(total)

def part_two():
    with open(filename) as file:
        lines = [parse_line_two(line.strip()) for line in file]
        print(lines)
        lines = sorted(lines, key=cmp_to_key(compare_card_two))
        print(lines)
        total = 0
        for i in range(len(lines)):
            total = total + (i + 1) * lines[i][2]
        print(total)

# part_one()
part_two()


