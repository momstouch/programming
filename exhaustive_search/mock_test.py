# https://programmers.co.kr/learn/courses/30/lessons/42840
import operator


def solution(answers):
    n = len(answers)
    loosers =[
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            ]
    result = []
    cutline = 0
    for idx, looser in enumerate(loosers, start = 1):
        mult = 1 if n <= len(looser) else int(n / len(looser)) + 1
        result.append([idx, sum([x == y for x, y in zip(answers, looser * mult)])])
        if cutline < result[-1][1]:
            cutline = result[-1][1]

    result.sort(
            reverse = True,
            key = operator.itemgetter(1)
            )

    return [rows[0] for rows in result if rows[1] == cutline]

answers = [1, 2, 3, 4, 5]
# return [1]
print(solution(answers))
