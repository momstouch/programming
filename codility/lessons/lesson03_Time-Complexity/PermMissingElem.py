# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):
    n = len(A) + 1

    return (n * (n + 1)) // 2 - sum(A)


cases = [
        ([2,3,1,5], 4),
        ]
for a, gt in cases:
    assert solution(a) == gt
