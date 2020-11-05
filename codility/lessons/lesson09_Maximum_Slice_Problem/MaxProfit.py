# https://app.codility.com/c/run/trainingDQ638E-6N8/


def solution(A):
    if not A:
        return 0

    ans = 0
    buy = A[0]

    for sell in A[1:]:
        if buy > sell:
            buy = sell
        else:
            gap = sell - buy
            if gap > ans:
                ans = gap

    return ans


cases = [
        [23171, 21011, 21123, 21366, 21013, 21367],     # 356
        []
        ]
for A in cases:
    print(solution(A))
