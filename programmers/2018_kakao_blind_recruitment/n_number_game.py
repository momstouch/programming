# https://programmers.co.kr/learn/courses/30/lessons/17687
NOTATION = "0123456789ABCDEF"

def numeral(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return (numeral(q, base) + n) if q else n

def solution(n, t, m, p):
    seq = ""
    i = 0
    while len(seq) < t * m:
        str_vals = numeral(i, n)
        seq += str_vals
        i += 1

    pick = [False] * m
    pick[p - 1] = True
    pick = pick * t

    return "".join(s for s, p in zip(seq, pick) if p)


cases = [
        (2, 4, 2, 1, "0111"),
        (16, 16, 2, 1, "02468ACE11111111"),
        (16, 16, 2, 2, "13579BDF01234567"),
        ]
for n, t, m, p, answer in cases:
    assert solution(n, t, m, p) == answer
