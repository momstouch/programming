# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    students = [
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            ]
    size = len(answers)
    ans = []
    maxval = 0

    for i, stu in enumerate(students, start = 1):
        tobe = size // len(stu) + 1
        stu = stu * tobe
        correct = 0
        for a, s in zip(answers, stu):
            correct += 1 if a == s else 0

        if maxval < correct:
            maxval = correct
            ans = [i]
        elif maxval == correct:
            ans.append(i)

    return sorted(ans)


def solution2(answers):
    students = [
            [1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
            ]
    scores = [0] * len(students)

    for i, a in enumerate(answers):
        for j, st in enumerate(students):
            scores[j] += 1 if st[i % len(st)] == a else 0

    maxscore = max(scores)
    result = []
    for i, s in enumerate(scores, start = 1):
        if s == maxscore:
            result.append(i)

    return result


cases = [
        [1, 2, 3, 4, 5],    # [1]
        [1, 3, 2, 4, 2],    # [1, 2, 3]
        ]
for case in cases:
    print(solution2(case))
