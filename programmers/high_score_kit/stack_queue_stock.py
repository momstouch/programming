# https://programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    ip = [(i, p) for i, p in enumerate(prices)]
    stack = [ip[0]]
    sec = 1

    ans = [0] * len(prices)

    for (i, p) in ip[1: ]:
        while stack and stack[-1][1] > p:
            idx, price = stack.pop()
            ans[idx] = sec - idx
        stack.append((i, p))

        sec += 1

    sec -= 1

    while stack:
        (i, p) = stack.pop()
        ans[i] = sec - i

    return ans


cases = [
        [1, 2, 3, 2, 3],        # [4, 3, 1, 1, 0]
        [50, 100, 1, 1, 1],     # [2, 1, 2, 1, 0]
        ]
for c in cases:
    print(solution(c))
