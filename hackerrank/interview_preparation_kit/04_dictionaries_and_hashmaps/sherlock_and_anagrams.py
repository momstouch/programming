# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter
def sherlockAndAnagrams(s):
    bucket = {}

    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i: i + j]).items())
            bucket[key] = bucket.get(key, 0) + 1
    ans = 0
    for key in bucket.keys():
        ans += (bucket[key] * (bucket[key] - 1)) // 2

    return ans

cases = [
        ("abba", 4),
        ("abcd", 0),
        ("ifailuhkqq", 3),
        ("kkkk", 10),
        ("cdcd", 5),
        ]
for s, answer in cases:
    assert sherlockAndAnagrams(s) == answer
