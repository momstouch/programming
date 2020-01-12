# https://programmers.co.kr/learn/courses/30/lessons/42841
#from itertools import permutations
from collections import Counter


def solution(baseball):
    #perms = list(map(''.join, permutations("123456789", 3)))

    answer = 0
    for i in range(123, 988):
        i = str(i)
        if '0' in i:
            continue
        i_counter = Counter(i)
        if len(i_counter) != 3:
            continue

        flag = True
        for perm, s, b in baseball:
            perm = str(perm)

            strike = sum([x == y for x, y in zip(i, perm)])
            ball = (3 - len(i_counter - Counter(perm))) - strike

            if strike != s or ball != b:
                flag = False
                break

        if flag:
            answer += 1

    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
# return 2

print(solution(baseball))
