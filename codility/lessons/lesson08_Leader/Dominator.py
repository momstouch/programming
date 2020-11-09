# https://app.codility.com/programmers/lessons/8-leader/dominator/


def solution(A):
    cnt = {}
    idx = {}

    for i, a in reversed(list(enumerate(A))):
        cnt[a] = cnt.get(a, 0) + 1
        idx[a] = i

    candidates = sorted(cnt.items(), key = lambda x: x[1])
    
    if not candidates or candidates[-1][1] <= len(A) // 2:
        return -1

    return idx[candidates[-1][0]]


cases = [
        ([3,4,3,2,3,-1,3,3], 0), # or 2,3,6,7
        ]
for a, gt in cases:
    assert solution(a) == gt
