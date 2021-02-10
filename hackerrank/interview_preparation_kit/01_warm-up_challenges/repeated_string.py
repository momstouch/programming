# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def repeatedString(s, n):
    slen = len(s)
    d, m = divmod(n, slen)
    acnt = s.count('a')

    return acnt * d + s[: m].count('a')

cases = [
        ("aba", 10, 7),
        ("a", 1000000000000, 1000000000000),
        ]
for s, n, answer in cases:
    assert repeatedString(s, n) == answer
