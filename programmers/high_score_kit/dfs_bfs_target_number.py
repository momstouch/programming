# https://programmers.co.kr/learn/courses/30/lessons/43165
import time


def dfs(num, numbers, i, target):
    if i == len(numbers):
        if num == target:
            return 1
        else:
            return 0

    return dfs(num + numbers[i], numbers, i + 1, target) + \
            dfs(num - numbers[i], numbers, i + 1, target)


def solution(numbers, target):
    return dfs(0, numbers, 0, target)


def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution2(numbers[1:], target + numbers[0]) + \
                solution2(numbers[1:], target - numbers[0])

# pythonic!
from itertools import product
def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    print(map(sum, product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)


cases = [
        [[1, 1, 1, 1, 1], 3],   # 5
        ]

t0 = time.time()
for case in cases:
    print(solution(case[0], case[1]))
print("%0.6f" % (time.time() - t0))

t0 = time.time()
for case in cases:
    print(solution2(case[0], case[1]))
print("%0.6f" % (time.time() - t0))

t0 = time.time()
for case in cases:
    print(solution3(case[0], case[1]))
print("%0.6f" % (time.time() - t0))
