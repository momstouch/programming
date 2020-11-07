# https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
from collections import Counter

def solution(A):
    A = list(filter(lambda x: x > 0, A))
    if not A:
        return 1

    A = sorted(Counter(A).keys())
    for i, a in enumerate(A, 1):
        if i < a:
            return i
    return A[-1] + 1


cases = [
        ([1,3,6,4,1,2], 5),
        ([1,2,3], 4),
        ([-1,-3], 1),
        ]
for a, gt in cases:
    assert solution(a) == gt
