# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

from collections import Counter
def countTriplets(arr, r):
    ans = 0
    j = Counter()
    k = Counter() 

    for x in arr:
        ans += k.get(x, 0)
        if x in j:
            k[x * r] += j[x]
        j[x * r] += 1

    return ans

cases = [
        (2, [1,2,2,4], 2),
        (3, [1,3,9,9,27,81], 6),
        (5, [1,5,5,25,125], 4),
        (2, [1,2,1,2,4], 3),
        ]
for r, arr, answer in cases:
    assert countTriplets(arr, r) == answer
