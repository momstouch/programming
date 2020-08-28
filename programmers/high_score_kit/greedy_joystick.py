# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    asciis = [ord(c) - ord('A') for c in name]
    target = len(name)

    n_alpha = ord('Z') - ord('A') + 1
    center = n_alpha // 2

    ans = 0
    last_pos = 0
    for i, num in enumerate(asciis):
        if num: # if alphabet is not an A
            if num > center:
                ans += n_alpha - num
            else:
                ans += num

            back = min(i, last_pos) - max(i, last_pos) + target
            front = abs(i - last_pos)

            ans += min(back, front)

            last_pos = i

    return ans


cases = [
        "JEROEN",       # 56
        "JAN",          # 23
        "BABBAABA",     # 9
        "BBBBAABB",     # 9
        ]

for case in cases:
    print(solution(case))
