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


def solution(number, k):
    target_len = len(number) - k
    number_ = [(n, i) for i, n in enumerate(number)]
    ans = ['0'] * target_len

    selected_id = 0
    for i in range(1, target_len + 1):
        print(selected_id, k + i)
        if number_[selected_id] == '9':
            j = selected_id
            max_val = '9'
        else:
            (max_val, j) = sorted(
                    number_[selected_id: k + i],
                    key = lambda x: x[0],
                    reverse = True)[0]
        selected_id = j + 1
        ans[i - 1] = max_val

    return "".join(ans)
            


cases = [
        ["1924", 2],        # "94"
        ["1231234", 3],     # "3234"
        ["4177252841", 4],  # "775841"
        ]
for number, k in cases:
    print(solution(number, k))
