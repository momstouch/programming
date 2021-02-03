from collections import Counter

def solution(before, after):
    if Counter(after) == Counter(before):
        return "NOT CHEATER"
    return "CHEATER"


T = int(input())
for _ in range(T):
    n = int(input())
    cards = [input() for _ in range(2)]
    cards = [c.split(" ") for c in cards]
    print(solution(cards[0], cards[1]))
