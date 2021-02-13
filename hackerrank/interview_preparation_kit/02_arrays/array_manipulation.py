# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# TODO: try to solve this problem later

def arrayManipulation(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        a -= 1
        arr[a] += k
        if b < n:
            arr[b] -= k

    max_ = 0
    x = 0 
    for a in arr:
        x += a
        max_ = max(max_, x)

    return max_


cases = [
        (
            5,
            [[1,2,100],[2,5,100],[3,4,100]],
            200
            ),
        (
            10,
            [[1,5,3],[4,8,7],[6,9,1]],
            10
            )
        ]
for n, queries, answer in cases:
    assert arrayManipulation(n, queries) == answer
