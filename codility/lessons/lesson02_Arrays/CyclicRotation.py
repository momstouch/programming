# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):
    if not A:
        return []

    k = K % len(A)

    return A[-k:] + A[:-k]


cases = [
        ([3,8,9,7,6], 3, [9,7,6,3,8]),
        ([0,0,0], 1, [0,0,0]),
        ([1,2,3,4], 4, [1,2,3,4]),
        ]
for a, k, gt in cases:
    assert solution(a, k) == gt
