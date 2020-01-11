# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    return str(int(
        ''.join(
            sorted(
                list(map(str, numbers)), # to be str from int
                reverse = True,  # Dec sort
                key = lambda x: x * 3 # to be max length
                )
            )
        ))


numbers = [6, 10, 2]
# return = "6210"
numbers = [3, 30, 34, 5, 9]
# return = "9534330"
print(solution(numbers))
