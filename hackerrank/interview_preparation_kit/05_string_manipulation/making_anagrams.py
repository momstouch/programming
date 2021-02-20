# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

from collections import Counter
def makeAnagram(a, b):
    ac = Counter(a)
    bc = Counter(b)

    ans = 0
    for k, v in ac.items():
        if k in bc:
            ans += abs(v - bc[k])
            bc.pop(k)
        else:
            ans += v

    return sum(bc.values())

def makeAnagram2(a, b):
    ac = Counter(a)
    bc = Counter(b)
    ac.subtract(bc)
    return sum(abs(x) for x in ac.values())

cases = [
        ("cde", "abc", 4),
        ]
for a, b, answer in cases:
    assert makeAnagram2(a, b) == answer
