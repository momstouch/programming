# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    ans = []
    for i, j, k in commands:
        ans.append(sorted(array[i - 1: j])[k - 1])

    return ans


cases = [
        [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]],#[5,6,3]
        ]

for array, commands in cases:
    print(solution(array, commands))
