# https://app.codility.com/c/run/trainingVXW6ZE-6DE/

from collections import Counter

def get_f(n):
    f = [0] * (n + 1)
    i = 2

    while i * i <= n:
        if f[i] == 0:
            k = i * i
            while k <= n:
                f[k] = i
                k += i
        i += 1

    return f

def solution(A):
    n = len(A) 
    f = get_f(n * 2 + 1)
    f[1], f[2], f[3] = 1, 2, 3

    a_cnt = Counter(A)
    ans = []

    for i in range(n):
        a = A[i]

        tmp = cnt = a_cnt[a]
        a_cnt[a] = 0
        while f[a] > 1:
            cnt += a_cnt.get(f[a], 0) 
            a = a // f[a]
        cnt += a_cnt.get(a, 0)
        a_cnt[A[i]] = tmp

        ans.append(n - cnt)

    print(ans)
    return ans


cases = [
        ([3,1,2,3,6], [2,4,3,2,0]),
        ([4,4], [0,0]),
        ([2,4], [1,0]),
        ]
for A, ans in cases:
    assert solution(A) == ans
