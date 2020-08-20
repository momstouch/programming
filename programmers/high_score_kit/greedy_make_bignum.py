# https://programmers.co.kr/learn/courses/30/lessons/42883
from itertools import combinations

def solution_timeover(number, k):
    target_len = len(number) - k
    return max(list(map("".join, combinations(number, target_len))))


def solution_timeover2(number, k):
    target_len = len(number) - k
    ans = sorted(combinations(number, target_len), reverse = True)[0]
    return "".join(ans)


def solution_timeover3(number, k):
    perms = number
    for i in range(1, k + 1):
        npick = len(number) - i
        perms = sorted(map("".join, combinations(perms, npick)), reverse = True)[0]

    return perms


def solution_timeover4(number, k):
    target_len = len(number) - k
    number_ = [(n, i) for i, n in enumerate(number)]
    ans = ['0'] * target_len

    selected_id = 0
    for i in range(1, target_len + 1):
        (max_val, j) = sorted(
                number_[selected_id: k + i],
                key = lambda x: x[0],
                reverse = True)[0]
        selected_id = j + 1
        ans[i - 1] = max_val

    return "".join(ans)


def solution_fake(number, k):
    target_len = len(number) - k
    ans = ['0'] * target_len

    selected_id = 0
    for i in range(1, target_len + 1):
        max_num = '0'
        for j in range(selected_id, k + i):
            n = number[j]
            if max_num < n:
                max_num = n
                selected_id = j + 1
                if max_num == '9':
                    break

        ans[i - 1] = max_num

    return "".join(ans)


def solution(number, k):
    stack = []
    n_len = len(number)

    for i, n in enumerate(number, 1):
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    # once k is not 0, it has to be removed
    return "".join(stack[: len(stack) - k])


cases = [
        ["1924", 2],        # "94"
        ["1231234", 3],     # "3234"
        ["4177252841", 4],  # "775841"
        ["100000", 2]
        ]
for number, k in cases:
    print(solution(number, k))
