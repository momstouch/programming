# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/

import math

def solution(N):
    ans = 2 * (1 + N)
    
    for n in range(2, math.ceil(math.sqrt(N)) + 1, 1):
        if N % n == 0:
            peri = 2 * (n + (N // n))
            ans = min(ans, peri)
    
    return ans


cases = [
        (30, 22),
        ]
for n, gt in cases:
    assert solution(n) == gt
