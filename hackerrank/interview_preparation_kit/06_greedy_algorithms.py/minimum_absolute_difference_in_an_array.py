# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

def minimumAbsoluteDifference(arr):
    a = sorted(arr)

    ans = max(arr)
    for x, y in zip(a[:-1], a[1:]):
        ans = min(abs(x - y), ans)

    return ans

cases = [
        ([3,-7,0], 3),
        ([-59,-36,-13,1,-53,-92,-2,-96,-54,75], 1),
        ([1,-3,71,68,17], 3),
        ]
for arr, answer in cases:
    assert minimumAbsoluteDifference(arr) == answer
