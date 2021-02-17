# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

def twoStrings(s1, s2):
    if set(s1) & set(s2):
        return "YES"
    return "NO"

cases = [
        ("hello", "world", "YES"),
        ("hi", "world", "NO"),
        ]
for s1, s2, answer in cases:
    assert twoStrings(s1, s2) == answer
