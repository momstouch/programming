# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/


def solution(A, B, K):
    beg = (A // K) - (1 if A % K == 0 else 0)
    end = B // K

    return end - beg


cases = [
        ((6, 11, 2), 3),
        ]
for (a, b, k), gt in cases:
    assert solution(a, b, k) == gt
