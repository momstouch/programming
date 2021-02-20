# https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

# longest common subsequence (LCS) problem
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def commonChild(s1, s2):
    memo = [0] * (len(s2) + 1)

    for i in range(1, len(s1) + 1):
        prev = 0
        for j in range(1, len(s2) + 1):
            temp = memo[j]
            if s1[i - 1] == s2[j - 1]:
                memo[j] = prev + 1
            elif memo[j] < memo[j - 1]:
                # max() makes this slower
                memo[j] = memo[j - 1]
            prev = temp

    return memo[-1]

cases = [
        ("HARRY", "SALLY", 2),
        ("AA", "BB", 0),
        ("SHINCHAN", "NOHARAAA", 3),
        ("ABCDEF", "FBDAMN", 2),
        ]
for s1, s2, answer in cases:
    assert commonChild(s1, s2) == answer
