# https://programmers.co.kr/learn/courses/30/lessons/42839
import itertools

def solution(numbers):
    answer = 0
    #perms = list(map(''.join, itertools.permutations(numbers)))
    perms = []
    primes = {}
    for i in range(1, len(numbers) + 1):
        perms.extend([list(x) for x in itertools.permutations(numbers, i)])
    for p in perms:
        p = int("".join([x for x in p]))
        flag = True
        for i in range(2, p // 2 + 1):
            if p % i == 0:
                flag = False
                break
        if flag:
            if p != 0 and p != 1:
                primes[p] = 1

    return len(primes)


def better_solution(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, itertools.permutations(numbers, i + 1))))
    a -= set(range(0, 2))

    # Eratos
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))

    return len(a)


cases = [
        "17",       # 3
        "011",      # 2
        ]

for case in cases:
    print(solution(case))
    print(better_solution(case))
