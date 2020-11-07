# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/


def solution(A):
    n = [0]

    cnt = 0
    for a in reversed(A):
        if a == 0:
            n.append(n[-1] + cnt)
            cnt = 0
        elif a == 1:
            cnt += 1

    ans = sum(n)
    return -1 if ans > 1000000000 else ans


cases = [
        ([0,1,0,1,1], 5),
        ]
for a, gt in cases:
    assert solution(a) == gt
