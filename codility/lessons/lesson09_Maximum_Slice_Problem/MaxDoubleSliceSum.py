# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/


def solution (A):
    A = A[1: -1]
    xy = [0]
    yz = [0]

    acc = 0
    for a in A[:-1]:
        acc = max(0, acc + a)
        xy.append(acc)
    acc = 0
    for a in reversed(A[1:]):
        acc = max(0, acc + a)
        yz.append(acc)

    return max(map(sum, zip(xy, reversed(yz))))


cases = [
        ([3,2,6,-1,4,5,-1,2], 17),
        ([0, 10, -5, -2, 0], 10),
        ]
for a, ans in cases:
    assert solution(a) == ans
