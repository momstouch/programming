# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    ans = i = 0
    n = len(c)
    while i < n - 1:
        if i + 2 >= n or c[i + 2] == 0:
            i += 2
        else:
            i += 1

        ans += 1

    return ans

cases = [
        (7, [0, 0, 1, 0, 0, 1, 0], 4),
        (6, [0, 0, 0, 0, 1, 0], 3),
        (6, [0, 0, 0, 1, 0, 0], 3),
        ]
for n, c, answer in cases:
    assert jumpingOnClouds(c) == answer
