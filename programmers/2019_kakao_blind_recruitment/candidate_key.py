# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations
from operator import itemgetter

def a_issubsetof_b(a, b):
    aa = set(a)
    for bb in b:
        if bb.issubset(aa):
            return True

    return False

def solution(relation):
    n_cols = len(relation[0])
    n_row = len(relation)
    candi = []

    comb = []
    for i in range(1, n_cols + 1):
        comb.extend(combinations(range(n_cols), i))

    for c in comb:
        if a_issubsetof_b(c, candi):
            continue
        itg = itemgetter(*c)
        if len(set([itg(row) for row in relation])) == n_row:
            candi.append(set(c))

    return len(candi)

cases = [
        (
            [
                ["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]
                ],
            2),
        ]
for relation, answer in cases:
    assert solution(relation) == answer
