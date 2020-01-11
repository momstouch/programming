# https://programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for [i, j, k] in commands:
        answer += [sorted(array[i - 1:j])[k - 1]]

    return answer


def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# return [5, 6, 3]

print(solution(array, commands))
print(solution2(array, commands))
