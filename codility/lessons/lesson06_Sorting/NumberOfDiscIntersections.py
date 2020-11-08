# https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/

def solution(A):
    lo = [0] * len(A)
    up = [0] * len(A)
    for i, a in enumerate(A):
        lo[i] = i - a
        up[i] = i + a

    lo.sort(reverse = True)
    up.sort(reverse = True)

    cur = ans = 0
    while lo:
        if lo[-1] <= up[-1]:
            ans += cur
            cur += 1
            lo.pop()
        else:
            up.pop()
            cur -= 1

    return -1 if ans > 10000000 else ans


cases = [
        ([1,0,1,0,1], 6),
        ([1,5,2,1,4,0], 11),
        ]
for a, gt in cases:
    assert solution(a) == gt
