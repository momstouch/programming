# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/


def solution(A):
    ans = 0

    for a in A:
        ans ^= a

    return ans


cases = [
        ([9,3,9,3,9,7,9], 7),
        ]
for a, ans in cases:
    assert solution(a) == ans
