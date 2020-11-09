# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

import math

def solution(N):
    cnt = {}

    for n in range(1, math.ceil(math.sqrt(N)) + 1):
        if N % n == 0:
            cnt[n] = 1
            cnt[N // n] = 1

    return len(cnt)


cases = [
        (24, 8),
        ]
for n, gt in cases:
    assert solution(n) == gt
