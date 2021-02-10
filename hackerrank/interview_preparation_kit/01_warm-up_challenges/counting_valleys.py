# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    ans = sea = 0
    vall = False
    for p in path:
        if p == "U":
            sea += 1
            if sea == 0 and vall:
                vall = False
                ans += 1
        elif p == "D":
            if sea == 0:
                vall = True
            sea -= 1

    return ans


cases = [
        (8, "UDDDUDUU", 1),
        (12, "DDUUDDUDUUUD", 2),
        ]
for steps, path, answer in cases:
    assert countingValleys(steps, path) == answer
