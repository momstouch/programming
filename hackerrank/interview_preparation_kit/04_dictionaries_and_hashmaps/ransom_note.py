# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter
def checkMagazine(magazine, note):
    mag = Counter(magazine)
    for w in note:
        rest = mag.get(w, 0) - 1
        if rest < 0:
            return "No"
        mag[w] = rest

    return "Yes"


cases = [
        (
            "give me one grand today night",
            "give one grand today",
            "Yes"
            ),
        (
            "two times three is not four",
            "two times two is four",
            "No"
            ),
        (
            "ive got a lovely bunch of coconuts",
            "ive got some coconuts",
            "No"
            ),
        ]
for magazine, note, answer in cases:
    magazine = list(magazine.split(" "))
    note = list(note.split(" "))
    assert checkMagazine(magazine, note) == answer
