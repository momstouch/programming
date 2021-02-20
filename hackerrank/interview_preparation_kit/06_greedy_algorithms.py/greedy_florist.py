# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms&h_r=next-challenge&h_v=zen

def getMinimumCost(k, c):
    ans = 0
    for i, x in enumerate(sorted(c, reverse = True)):
        order = i // k
        ans += (order + 1) * x

    return ans

cases = [
        (2, [2,5,6], 15),
        (3, [1,3,5,7,9], 29),
        ]
for k, c, answer in cases:
    assert getMinimumCost(k, c) == answer
