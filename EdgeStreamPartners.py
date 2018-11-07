

def poker(hands):
    best = max(hands, key=hand_rank_orig)
    return hand_rank(best), best


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return "straight-flush"
    elif kind(4, ranks):                           # 4 of a kind
        return "four-of-a-kind"
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return "full-house"
    elif flush(hand):                              # flush
        return "flush"
    elif straight(ranks):                          # straight
        return "straight"
    elif kind(3, ranks):                           # 3 of a kind
        return "three-of-a-kind"
    elif two_pair(ranks):                          # 2 pair
        return "two-pairs"
    elif kind(2, ranks):                           # kind
        return "one-pair"
    else:                                          # high card
        return "highest-card"


def hand_rank_orig(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    min_num = ranks[0]
    List = [min_num - i for i in range(len(ranks))]
    if List == ranks:
        return True
    else:
        return False


def flush(hand):
    "Return True if all the cards have the same suit."
    suit = [s for n, s in hand]
    if [suit[0]]*len(suit) == suit:
        return True
    else:
        return False


def kind(n, ranks):
    "Return the first rank that this hand has exactly n of.Return None if there is no n-of-a-kind in the hand."
    for r in ranks:
        if ranks.count(r) == n:
            return r

    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = []
    for i in set(ranks):
        if ranks.count(i) == 2:
            pair.append(i)
    if len(pair) == 2:
        return tuple(sorted(pair, reverse=True))
    else:
        return None


def card_ranks(hand):
    "return a list of the ranks , sorted with higher first"
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def card_ranks1(cards):
    "Return a list of the ranks, sorted with higher first."
    def map(r):
        if r == 'T':
            return 10
        elif r == 'J':
            return 11
        elif r == 'Q':
            return 12
        elif r == 'K':
            return 13
        elif r == 'A':
            return 14
        else:
            return int(r)
    ranks = [map(r) for r, s in cards]
    ranks.sort(reverse=True)

    return ranks

# def allmax(iterable ,key = None):
#     "return a list of all items equal to the max of the iterable"
#     result , maxval =[],None
#     key = key or (lambda: x:x)
#     for x in iterable:
#         xval = key(x)
#         if not result or xval > maxval:
#             result , maxval = [x] , xval
#         elif xval == maxval:
#             result.append(x)
#     return result


def printCombination(arr, n, r):
    data = [0]*r
    output = []
    combinationUtil(arr, data, 0,
                    n - 1, 0, r, output)
    return output


def combinationUtil(arr, data, start,
                    end, index, r, output):
    t = []
    if (index == r):
        for j in range(r):
            t.append(data[j])
        output.append(t)
        return
    i = start
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r, output)
        i += 1


a = [
    "2H 2S 3H 3S 3C",
    "TH JH QC QD QS",
    "KS AH 2H 3C 4H",
    "3D 4S 5S 6D 7H",
    "AD AS AH JD JS"
]
s = ["TH JH QC QD QS QH KH AH 2S 6S",
     "2H 2S 3H 3S 3C 2D 3D 6C 9C TH",
     "2H 2S 3H 3S 3C 2D 9C 3D 6C TH",
     "2H AD 5H AC 7H AH 6H 9H 4H 3C",
     "AC 2D 9C 3S KD 5S 4D KS AS 4C",
     "KS AH 2H 3C 4H KC 2C TC 2D AS",
     "AH 2C 9S AD 3C QH KS JS JD KD",
     "6C 9C 8C 2D 7C 2H TC 4C 9S AH",
     "3D 5S 2H QD TD 6S KH 9H AD QH"]

# Hand: TH JH QC QD QS Deck: QH KH AH 2S 6S Best hand: straight-flush
# Hand: 2H 2S 3H 3S 3C Deck: 2D 3D 6C 9C TH Best hand: four-of-a-kind
# Hand: 2H 2S 3H 3S 3C Deck: 2D 9C 3D 6C TH Best hand: full-house
# Hand: 2H AD 5H AC 7H Deck: AH 6H 9H 4H 3C Best hand: flush
# Hand: AC 2D 9C 3S KD Deck: 5S 4D KS AS 4C Best hand: straight
# Hand: KS AH 2H 3C 4H Deck: KC 2C TC 2D AS Best hand: three-of-a-kind
# Hand: AH 2C 9S AD 3C Deck: QH KS JS JD KD Best hand: two-pairs
# Hand: 6C 9C 8C 2D 7C Deck: 2H TC 4C 9S AH Best hand: one-pair
# Hand: 3D 5S 2H QD TD Deck: 6S KH 9H AD QH Best hand: highest-card


def eval_deck(total):
    r = 5
    n = len(total)
    hands = printCombination(total, n, r)
    return poker(hands)


for i in s:
    line = i.split(' ')
    print("Hand: {hand} Deck: {deck} Best hand: {best}".format(
        hand=i[:13], deck=i[13:], best=eval_deck(line)))
    # print(eval_deck(line))
