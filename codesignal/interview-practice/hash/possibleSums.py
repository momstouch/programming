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
    ans = set([0]) # set for accumulation results
    for i, coin in enumerate(coins):
        inner = set()
        for q in range(0, quantity[i] + 1):
            for s in ans:
                # for sum of all possible combinations of coins
                inner.add(s + coin * q)

        # union two sets
        ans = ans | inner

    return len(ans) - 1


cases = [
        [[10, 50, 100], [1, 2, 1]],             # 9
        [[10, 50, 100, 500], [5, 3, 2, 2]],     # 122
        ]
for coins, quantity in cases:
    print(possibleSums(coins, quantity))
