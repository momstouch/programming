# https://programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    cloth_dict = {}
    for cloth, kind in clothes:
        cloth_dict[kind] = cloth_dict.get(kind, []) + [cloth]

    values = [len(x) for x in cloth_dict.values()]

    answer = 1
    for v in values:
        answer = answer * (v + 1) # +1 means that not wearing v

    return answer - 1


from collections import Counter
from functools import reduce

def solution2(clothes):
    cloth_counter = Counter([ctype for _, ctype in clothes]) # <str, int>
    return reduce(lambda a, b: a + b + a * b, cloth_counter.values())


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# return 5

print(solution(clothes))
print(solution2(clothes))
