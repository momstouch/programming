# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    def dfs(numbers, index, target):
        if index == len(numbers):
            return 0 if target else 1

        return dfs(numbers, index + 1, target + numbers[index]) + \
                dfs(numbers, index + 1, target - numbers[index])

    return dfs(numbers, 0, target)


numbers = [1, 1, 1, 1, 1]
target = 3
# answer is 5
# numbers can be the target with the combination of + and -
# write the solution() to get the number of cases of all combination of numbers

print(solution(numbers, target))
