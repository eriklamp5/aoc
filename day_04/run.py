

def score_card(line):
    line = line.replace("Card ", "")
    line = line.split(":")
    card_num = int(line[0])
    line = line[1].strip().split("|")
    card_vals = [int(val.strip()) for val in line[0].strip().split(" ") if val != ""]
    winning_vals = [int(val.strip()) for val in line[1].strip().split(" ") if val != ""]
    
    # print(f"{card_num}: {card_vals} | {winning_vals}")

    score = 0
    for val in card_vals:
        if val in winning_vals:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score


def count_wins(line):
    line = line.replace("Card ", "")
    line = line.split(":")
    card_num = int(line[0])
    line = line[1].strip().split("|")
    card_vals = [int(val.strip()) for val in line[0].strip().split(" ") if val != ""]
    winning_vals = [int(val.strip()) for val in line[1].strip().split(" ") if val != ""]
    
    # print(f"{card_num}: {card_vals} | {winning_vals}")

    count = sum([1 if val in winning_vals else 0 for val in card_vals])

    return count

filename = "day_04/input.txt"
# filename = "day_04/example.txt"
with open(filename) as file:
    # total = sum([score_card(line.strip()) for line in file])
    # print(total)

    wins = [count_wins(line.strip()) for line in file]
    total_cards = 0
    duplicated_cards = [0] * len(wins)
    for i in range(len(wins)):
        # print(f"{i} {wins[i]}")
        if wins[i] != 0:
            for d in range(wins[i]):
                duplicated_cards[i + d + 1] += (duplicated_cards[i] + 1)
            # print(f"    {duplicated_cards}")
    print(len(wins) + sum(duplicated_cards))
        

