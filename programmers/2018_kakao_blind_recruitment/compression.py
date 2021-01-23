# https://programmers.co.kr/learn/courses/30/lessons/17684
import string

def solution(msg):
    ans = []
    dic = {c: i for i, c in enumerate(string.ascii_uppercase, start = 1)}
    dic_cnt = len(dic) + 1
    n = len(msg)
    i = 0

    while i < n:
        j = i + 1
        ans.append(-1)
        while j <= n:
            idx = dic.get(msg[i: j], -1)
            if idx < 0:
                dic[msg[i: j]] = dic_cnt
                dic_cnt += 1
                break
            else:
                ans[-1] = idx
            j += 1
        i += (j - i - 1)

    return ans


cases = [
        (
            "KAKAO",
            [11, 1, 27, 15]
            ),
        (
            "TOBEORNOTTOBEORTOBEORNOT",
            [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
            ),
        (
            "ABABABABABABABAB",
            [1, 2, 27, 29, 28, 31, 30]
            )
        ]
for msg, answer in cases:
    assert solution(msg) == answer
