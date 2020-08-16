# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    ans = -1
    for n, ci in enumerate(sorted(citations, reverse = True), 1):
        h = min(n, ci)
        if ans < h:
            ans = h
        else:
            break

    return ans


cases = [
        [3, 0, 6, 1, 5],        # 3
        ]
for case in cases:
    print(solution(case))
