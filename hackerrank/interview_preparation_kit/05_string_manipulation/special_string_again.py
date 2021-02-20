# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def substrCount(n, s):
    i = 0
    comp = []
    # squeeze s down to like [[a, 1], [b, 2], [c, 3]]
    while i < len(s):
        comp.append([s[i], 1])
        i += 1
        while i < len(s) and s[i] == comp[-1][0]:
            comp[-1][1] += 1
            i += 1

    ans = 0
    for i in range(len(comp)):
        x, cnt = comp[i]
        ans += cnt * (cnt + 1) // 2 # 1st condition
        if cnt == 1 and i > 0 and i + 1 < len(comp): # 2nd condition
            prev, p_cnt = comp[i - 1]
            next_, n_cnt = comp[i + 1]
            if prev == next_:
                ans += min(p_cnt, n_cnt)

    return ans

cases = [
        ("mnonopoo", 12),
        ("asasd", 7),
        ("abcbaba", 10),
        ("aaaa", 10),
        ]
for s, answer in cases:
    assert substrCount(len(s), s) == answer
