# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

from collections import Counter
def isValid(s):
    scnt = Counter(s)
    cnt = Counter()
    for x in scnt.values():
        cnt[x] += 1
    if len(cnt) == 1:
        return "YES"
    try:
        x, y = cnt.keys()
        if (abs(x - y) == 1 and cnt[max(x, y)] == 1) or \
                (min(x, y) == 1 and cnt[min(x, y)] == 1):
                    return "YES"
    except ValueError:
        pass
    return "NO"

cases = [
        ("aabbcd", "NO"),
        ("aabbccddeefghi", "NO"),
        ("abcdefghhgfedecba", "YES"),
        ]
for s, answer in cases:
    assert isValid(s) == answer
