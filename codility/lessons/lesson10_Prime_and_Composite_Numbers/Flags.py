# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/flags/

def solution(A):
    if len(A) < 3:
        return 0
        
    N = len(A)
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks[i] = True
    
    nextp = [0] * N
    nextp[N - 1] = -1
    for i in range(N - 2, -1, -1):
        if peaks[i]:
            nextp[i] = i
        else:
            nextp[i] = nextp[i + 1]

    for i in range(sum(peaks), 0, -1):
        pos = 0
        flags = 0
        while pos < N and flags < i:
            pos = nextp[pos]
            if pos < 0:
                break
            pos += i
            flags += 1
        if flags == i:
            return flags
    
    return 0


cases = [
        ([1,5,3,4,3,4,1,2,3,4,6,2], 3),
        ]
for a, gt in cases:
    assert solution(a) == gt
