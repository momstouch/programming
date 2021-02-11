# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

def rotLeft(a, b):
    length = (b // len(a) + int(b % len(a) > 0)) * len(a)
    new_head = length - b
    tobe_tail = len(a) - new_head
    return a[tobe_tail:] + a[:tobe_tail]

cases = [
        ([1,2,3,4,5], 4, [5,1,2,3,4]),
        ([1,2,3,4,5], 5, [1,2,3,4,5]),
        ([1,2], 3, [2,1]),
        ([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51],
            10,
            [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]),
        ]
for a, b, answer in cases:
    assert rotLeft(a, b) == answer
