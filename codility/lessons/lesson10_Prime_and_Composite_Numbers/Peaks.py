# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/peaks/

import math

def solution(A):
    N = len(A)
    
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks[i] = True

    accp = [0] * (N + 1)
    for i in range(1, N):
        if peaks[i - 1]:
            accp[i] = accp[i - 1] + 1
        else:
            accp[i] = accp[i - 1]
    accp[N] = accp[N - 1]

    ans = 0
    for blks in range(1, sum(peaks) + 1):
        if N % blks != 0:
            continue

        found = True
        k = N // blks
        for j in range(blks):
            if accp[j * k] == accp[j * k + k]:
                found = False
                break
        if found:
            ans = max(ans, blks)
        
    return ans


cases = [
        ([1,2,3,4,3,4,1,2,3,4,6,2], 3),
        ]
for a, gt in cases:
    assert solution(a) == gt
