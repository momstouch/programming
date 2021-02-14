# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen

def maximumToys(prices, k):
    total = 0
    for i, p in enumerate(sorted(prices), start = 0):
        if total + p < k:
            total += p
        else:
            return i

    return len(prices)


cases = [
        (50, [1,12,5,111,200,1000,10], 4),
        ]
for k, prices, answer in cases:
    assert maximumToys(prices, k) == answer
