# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def alternatingCharacters(s):
    prev = s[0]
    ans = 0
    for c in s[1:]:
        if prev == c:
            ans += 1
        prev = c

    return ans

cases = [
        ("AAAA", 3),
        ("BBBBB", 4),
        ("ABABABAB", 0),
        ("BABABA", 0),
        ("AAABBB", 4),
        ]
for s, answer in cases:
    assert alternatingCharacters(s) == answer
