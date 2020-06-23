from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = list(Counter([key[1] for key in clothes]).values())
    answer = reduce(lambda x, y: x * (y + 1), cnt, 1) - 1

    return answer


cases = [
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"]], # answer: 5
        [
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"]] # answer: 3
        ]

for c in cases:
    print(solution(c))
