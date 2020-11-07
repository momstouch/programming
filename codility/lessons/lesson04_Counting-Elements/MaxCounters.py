# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

def solution(N, A):
    mcnt = 0
    mcnt_do = 0
    cnt = [0] * N
    for k in A:
        if k <= N:
            cnt[k - 1] = max(mcnt_do, cnt[k - 1]) + 1
            mcnt = max(cnt[k - 1], mcnt)
        elif k == N + 1:
            mcnt_do = mcnt

    for i in range(N):
        cnt[i] = max(cnt[i], mcnt_do)
    return cnt


cases = [
        (1, [1], [1]),
        (5, [3,4,4,6,1,4,4], [3,2,2,4,2]),
        ]
for n, a, gt in cases:
    assert solution(n, a) == gt
