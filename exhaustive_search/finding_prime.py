# https://programmers.co.kr/learn/courses/30/lessons/42839


def prime(number):
    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if (number % i) == 0:
                return False
        return True
    return False


# TODO:
# recur cannot make all permutations
def recur(numbers, idx, num, answer):
    if idx < len(numbers):
        num += numbers[idx]
        print(num)
        if prime(int(num)):
            answer[int(num)] = 1

        for i in range(1, len(numbers)):
            recur(numbers, idx + i, num, answer)
        for i in range(1, len(numbers)):
            recur(numbers, idx + i, num[:-1], answer)


def solution(numbers):
    answer = {}
    for idx, n in enumerate(numbers):
        recur(numbers[idx] + numbers[0:idx] + numbers[idx + 1:], 0, "", answer)

    return len(answer)


from itertools import permutations
def solution2(numbers):
    answer = {}
    for i in range(1, len(numbers) + 1):
        for val in list(map(int, map(''.join, permutations(numbers, i)))):
            if prime(val):
                answer[val] = 1

    return len(answer)


numbers = "17"
# return 3
numbers = "011"
# return 2

testcase = ["17", "011"]
for t in testcase:
    print("start")
    print(solution2(t))
    print("end")
