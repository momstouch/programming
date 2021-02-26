# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

def maxMin(k, arr):
    ans = 10 ** 9
    arr.sort()
    for i in range(0, len(arr) - k + 1):
        ans = min(ans, arr[i+k-1] - arr[i])

    return ans

cases = [
        (3, [10, 100, 300, 200, 1000, 20, 30], 20),
        (4, [1,2,3,4,10,20,30,40,100,200], 3),
        (2, [1,2,1,2,1], 0),
        ]
for k, arr, answer in cases:
    assert maxMin(k, arr) == answer
