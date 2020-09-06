# https://app.codesignal.com/interview-practice/task/rMe9ypPJkXgk3MHhZ

from itertools import combinations
from collections import Counter

def possibleSums_exceed_time_limit(coins, quantity):
    c = []
    for coin, q in zip(coins, quantity):
        c += [coin] * q

    comb = [(cc,) for cc in coins]
    for r in range(2, len(c) + 1):
        comb.extend(combinations(c, r)) 
    comb = Counter(map(sum, comb))

    return len(comb)


def possibleSums(coins, quantity):
    poss = [] # possibilities
    for coin, quan in zip(coins, quantity):
        poss.append([coin * q for q in range(quan + 1)])

    ans = set(map(sum, *product(poss)))
    print(ans)


cases = [
        [[10, 50, 100], [1, 2, 1]],             # 9
        [[10, 50, 100, 500], [5, 3, 2, 2]],     # 122
        ]
for coins, quantity in cases:
    print(possibleSums(coins, quantity))
