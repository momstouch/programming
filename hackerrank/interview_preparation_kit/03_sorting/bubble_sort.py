# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

def countSwaps(a):
    n_swap = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                n_swap += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    return n_swap

cases = [
        ([6,4,1], 3),
        ]
for a, answer in cases:
    assert countSwaps(a) == answer
