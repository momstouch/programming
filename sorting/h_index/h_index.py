# https://programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    for i, c in enumerate(sorted(citations, reverse = True)):
        if i + 1 > c:
            return i
    return len(citations)


def solution_veteran(citations):
    citations.sort(reverse = True)
    return max(map(min, enumerate(citations, start = 1)))


citations = [3, 0, 6, 1, 5]
# return 3

citations = [22, 42]
# return 2

citations = [20, 19, 18, 1]
# return 3

print(solution(citations))
