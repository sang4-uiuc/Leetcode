
def getBestHand(hands):
    """
    Return the best hand name and corresponding deck
    """
    best = max(hands, key=rankHand)
    return getName(best), best


def getName(hand):
    """
    Return name of the hand
    """
    ranks = rankCard(hand)
    if straight(ranks) and flush(hand):
        return "straight-flush"
    elif kind(4, ranks):
        return "four-of-a-kind"
    elif kind(3, ranks) and kind(2, ranks):
        return "full-house"
    elif flush(hand):
        return "flush"
    elif straight(ranks):
        return "straight"
    elif kind(3, ranks):
        return "three-of-a-kind"
    elif twoPair(ranks):
        return "two-pairs"
    elif kind(2, ranks):
        return "one-pair"
    else:
        return "highest-card"


def rankHand(hand):
    """
    Return a number comparing the hand
    Stronger the hand, higher the number
    """
    ranks = rankCard(hand)
    if straight(ranks) and flush(hand):
        return 8
    elif kind(4, ranks):
        return 7
    elif kind(3, ranks) and kind(2, ranks):
        return 6
    elif flush(hand):
        return 5
    elif straight(ranks):
        return 4
    elif kind(3, ranks):
        return 3
    elif twoPair(ranks):
        return 2
    elif kind(2, ranks):
        return 1
    else:
        return 0


def straight(ranks):
    """
    Return true if it's a straight
    """
    minNum = ranks[0]
    List = [minNum - i for i in range(len(ranks))]
    if List == ranks:
        return True
    else:
        return False


def flush(hand):
    """
    Return True if it's a flush
    """
    suit = [s for n, s in hand]
    if [suit[0]]*len(suit) == suit:
        return True
    else:
        return False


def kind(n, ranks):
    """
    Return the rank if has exactly n of
    Return None if there isn't any
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r

    return None


def twoPair(ranks):
    """
    Return two ranks as a tuple if there are two pairs
    Return None otherwise
    """
    pair = []
    for i in set(ranks):
        if ranks.count(i) == 2:
            pair.append(i)
    if len(pair) == 2:
        return tuple(sorted(pair, reverse=True))
    else:
        return None


def rankCard(hand):
    """
    Return a sorted list of the ranks 
    """
    
    for r, s in hand:
        ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

# This one doesn't work because I realized that Ace can also act as 1
# def rankCard1(cards):
#     """
#     Return a list of the ranks
#     """
#     def map(r):
#         if r == 'T':
#             return 10
#         elif r == 'J':
#             return 11
#         elif r == 'Q':
#             return 12
#         elif r == 'K':
#             return 13
#         elif r == 'A':
#             return 14
#         else:
#             return int(r)
#     ranks = [map(r) for r, s in cards]
#     ranks.sort(reverse=True)

#     return ranks


def getCombinations(arr, n, r, deck):
    """
    Return all combination of the given cards
    """
    data = [0]*r
    output = []
    for i in range(r):
        combinationUtil(arr, data, 0,
                    n - 1, 0, r - i, output)
    
    for l in output:
        if len(l) == 4:
            for i in deck[:1]:
                l.append(i)
        elif len(l) == 3:
            for i in deck[:2]:
                l.append(i)
        elif len(l) == 2:
            for i in deck[:3]:
                l.append(i)
        elif len(l) == 1:
            for i in deck[:4]:
                l.append(i)
    output.append(deck)
    # print(output)
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

z = ["TH JH QC QD QS QH KH AH 2S 6S"]
def evalDeck(total):
    orig = total[:5]
    deck = total[5:]
    r = 1
    n = len(orig)
    hands = getCombinations(orig, n, 5, deck)
    return getBestHand(hands)


for i in s:
    line = i.split(' ')
    bestHand = evalDeck(line)
    print("Hand: {hand} Deck: {deck} Best hand: {best} {card}".format(
        hand=i[:14], deck=i[15:], best=bestHand[0], card= " ".join(bestHand[1])))