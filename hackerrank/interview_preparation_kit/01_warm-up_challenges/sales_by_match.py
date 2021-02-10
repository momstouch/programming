# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Complete the sockMerchant function below.
from collections import Counter
def sockMerchant(n, ar):
    return sum([c // 2 for c in Counter(ar).values()])


cases = [
        (7, [1,2,1,2,1,3,2], 2),
        (9, [10, 20, 20, 10, 10, 30, 50, 10, 20], 3),
        ]
for n, ar, answer in cases:
    assert sockMerchant(n, ar) == answer
