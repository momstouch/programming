# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import OrderedDict


def solution(priorities, location):
    dict_q = OrderedDict({i: p for i, p in enumerate(priorities)})
    n_print = 0

    while dict_q:
        i, p = dict_q.popitem(last = False)

        if sum([p < p_in_q for p_in_q in dict_q.values()]):
            #dict_q.update({i: p})
            dict_q[i] = p
        else:
            n_print += 1
            if i == location:
                return n_print

    return n_print



cases = [
        [[2, 1, 3, 2], 2],          # 1
        [[1, 1, 9, 1, 1, 1], 0]     # 5
        ]
for c in cases:
    p, l = c
    print(solution(p, l))
