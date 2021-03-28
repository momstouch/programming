# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    counter = [0] * (N + 2)
    n_user = len(stages)

    for st in stages:
        counter[st] += 1

    result = []
    for i, x in enumerate(counter[1: -1], start = 1):
        n_try = sum(counter[i:])
        if n_try == 0:
            rate = 0
        else:
            rate = x / n_try

        result.append((rate, i))

    result.sort(reverse = True, key = lambda x: x[0])

    return list(map(lambda x: x[1], result))

cases = [
        (1, [2], [1]),
        (5, [2, 1, 2, 6, 2, 4, 3, 3], [3,4,2,1,5]),
        (4, [4,4,4,4,4], [4,1,2,3]),
        ]
for N, stages, answer in cases:
    assert solution(N, stages) == answer
