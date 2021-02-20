# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import heapq
def luckBalance(k, contests):
    ans = 0
    imp_cont = []
    for luck, imp in contests:
        if imp == 0:
            ans += luck
        else:
            heapq.heappush(imp_cont, luck)

    for _ in range(len(imp_cont) - k):
        ans -= heapq.heappop(imp_cont)

    while imp_cont:
        ans += heapq.heappop(imp_cont)

    return ans


cases = [
        (3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]], 29),
        ]
for k, contests, answer in cases:
    assert luckBalance(k, contests) == answer
