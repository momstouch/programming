# https://programmers.co.kr/learn/courses/30/lessons/42747

import time

def solution(citations):
    ans = -1
    for n, ci in enumerate(sorted(citations, reverse = True), 1):
        h = min(n, ci)
        if ans < h:
            ans = h
        else:
            break

    return ans

def solution2(citations):
    n = len(citations)
    cita = sorted(citations, reverse = True)

    for h, c in enumerate(cita, start = 1):
        if h <= c and ((h < n and cita[h] <= h) or h == n):
            return h

    return 0

cases = [
        ([3, 0, 6, 1, 5], 3),
        ]

t0 = time.time()
for citations, answer in cases:
    assert solution(citations) == answer
print("%.6f" % (time.time() - t0))

t0 = time.time()
for citations, answer in cases:
    assert solution2(citations) == answer
print("%.6f" % (time.time() - t0))
