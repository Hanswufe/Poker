white_win = "White wins"
black_win = "Black wins"
tie = "Tie"

#Input a pair of poker hands and return who wins
#poker_hands format:"Black:2H 3D 5S 9C KD;White:2C 3H 4S 8C AH"
def Poker(pair_poker_hands):

    black_poker_hands, white_poker_hands = pair_poker_hands.split(';')
    black_poker_hands = black_poker_hands.split(':')[1].split(" ")
    white_poker_hands = white_poker_hands.split(':')[1].split(" ")
    black_kind_rank = get_kind_rank(black_poker_hands)
    white_kind_rank = get_kind_rank(white_poker_hands)
    if black_kind_rank < white_kind_rank:
        return white_win
    elif black_kind_rank > white_kind_rank:
        return black_win
    else:
        black_number = get_number(black_poker_hands)
        white_number = get_number(white_poker_hands)
        if black_kind_rank == 1:
            win = high_card(black_number,white_number)
            return win
        elif black_kind_rank == 2:
            win = pair(black_number,white_number)
            return win
        elif black_kind_rank == 3:
            win = two_pairs(black_number,white_number)
            return win
        elif black_kind_rank == 4:
            win = three_of_a_kind(black_number,white_number)
            return win
        elif black_kind_rank == 5:
            win = straight(black_number,white_number)
            return win
        elif black_kind_rank == 6:
            win = flush(black_number, white_number)
            return win
        elif black_kind_rank == 7:
            win = full_house(black_number, white_number)
            return win
        elif black_kind_rank == 8:
            win = four_of_a_kind(black_number, white_number)
            return win
        else:
            win = straight_flush(black_number, white_number)
            return win

def high_card(black_number, white_number):
    black_number = black_number[4] * 10000 + black_number[3] * 1000 + black_number[2] * 100 + black_number[1] * 10 + \
                   black_number[0] * 1
    white_number = white_number[4] * 10000 + white_number[3] * 1000 + white_number[2] * 100 + white_number[1] * 10 + \
                   white_number[0] * 1
    if black_number < white_number:
        return white_win
    elif black_number > white_number:
        return black_win
    else:
        return tie

def pair(black_number,white_number):
    black_same_number_dict = get_same_number(black_number)
    white_same_number_dict = get_same_number(white_number)
    black_pair_num = int((get_key(black_same_number_dict, 2))[0])
    white_pair_num = int((get_key(white_same_number_dict, 2))[0])
    if black_pair_num > white_pair_num:
        return black_win
    elif black_pair_num < white_pair_num:
        return black_win
    else:
        black_left_number = sorted(list(map(int, get_key(black_same_number_dict, 1))))
        white_left_number = sorted(list(map(int, get_key(white_same_number_dict, 1))))
        black_left_number = black_left_number[2] * 100 + black_left_number[1] * 10 + black_left_number[0] * 1
        white_left_number = white_left_number[2] * 100 + white_left_number[1] * 10 + white_left_number[0] * 1
        if black_left_number > white_left_number:
            return black_win
        elif black_left_number < white_left_number:
            return white_win
        else:
            return tie
def two_pairs(black_number, white_number):
    black_same_number_dict = get_same_number(black_number)
    white_same_number_dict = get_same_number(white_number)
    black_pair_num = sorted((get_key(black_same_number_dict, 2)))
    white_pair_num = sorted((get_key(white_same_number_dict, 2)))
    if black_pair_num[1] > white_pair_num[1]:
        return black_win
    elif black_pair_num[1] < white_pair_num[1]:
        return black_win
    else:
        if black_pair_num[0] > white_pair_num[0]:
            return black_win
        elif black_pair_num[0] < white_pair_num[0]:
            return black_win
        else:
            black_left_number = int(get_key(black_same_number_dict, 1)[0])
            white_left_number = int(get_key(white_same_number_dict, 1)[0])
            if black_left_number > white_left_number:
                return black_win
            elif black_left_number < white_left_number:
                return white_win
            else:
                return tie
def three_of_a_kind(black_number, white_number):
    return 0
def straight(black_number, white_number):
    return 0
def flush(black_number, white_number):
    return 0
def full_house(black_number, white_number):
    return 0
def four_of_a_kind(black_number, white_number):
    return 0
def straight_flush(black_number, white_number):
    return 0

def get_key(dict, value):
    return [k for (k, v) in dict.items() if v == value]

def is_same_suit(poker_hands):
    suit = [item[1] for item in poker_hands]
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
        return True
    return False

def get_number(poker_hands):
    re = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    number = [re[item[0]] if item[0] in re else int(item[0]) for item in poker_hands]
    number.sort()
    return number

def get_same_number(number):
    dict = {}
    for num in number:
        if num in dict.keys():
            dict[num] += 1
        else:
            dict[num] = 1
    return dict

def get_kind_rank(poker_hands):
    number = get_number(poker_hands)
    #print(number)
    if is_same_suit(poker_hands):
        if number[0]+1 == number[1] and number[1]+1 == number[2] and number[2]+1 == number[3] and number[3]+1 == number[4]:
            return 9
        return 6
    if number[0] + 1 == number[1] and number[1] + 1 == number[2] and number[2] + 1 == number[3] and number[3] + 1 == number[4]:
        return 5
    same_number_dict = get_same_number(number)
    max_same_num = max(same_number_dict.values())
    min_same_num = min(same_number_dict.values())
    if max_same_num == 4:
        return 8
    if max_same_num == 3:
        if min_same_num == 2:
            return 7
        return 4
    if max_same_num == 2:
        if len(same_number_dict) == 3:
            return 3
        return 2
    return 1
