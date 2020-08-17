# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    no_cloth = 0
    reserve_dict = {r : False for r in reserve}
    lost_dict = {l : False for l in lost}

    for l in lost:
        if not reserve_dict.pop(l, True):
            continue
        poped = reserve_dict.pop(l - 1, True)
        if poped and lost_dict.get(l + 1, True):
            poped = reserve_dict.pop(l + 1, True)
        no_cloth += poped
    return n - no_cloth


def solution2(n, lost, reserve):
    reserve_dict = {r: False for r in reserve if not r in lost}
    lost = [l for l in lost if not l in reserve]

    no_cloth = 0

    for l in lost:
        not_poped = reserve_dict.pop(l - 1, True)
        if not_poped:
            not_poped = reserve_dict.pop(l + 1, True)
        no_cloth += not_poped

    return n - no_cloth


cases = [
        [5, [2, 4], [1, 3, 5]],     # 5
        [5, [2, 4], [3]],           # 4
        [3, [3], [1]],              # 2
        [5, [2,3], [3,4]]           # 4
        ]
for n, lost, reserve in cases:
    print(solution2(n, lost, reserve))
