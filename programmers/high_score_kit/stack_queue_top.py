# https://programmers.co.kr/learn/courses/30/lessons/42588
import time


def solution(heights):
    answer = [0]
    for i, h in enumerate(heights[1:], 1):
        for j in range(i - 1, -2, -1):
            if j < 0:
                answer.append(0)
                break
            if heights[i] < heights[j]:
                answer.append(j + 1)
                break

    return answer


def solution2(heights):
    answer = [0] * len(heights)
    for i, j in enumerate(heights[1:], 1):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j + 1
                break

    return answer


cases = [
        [6, 9, 5, 7, 4],        # [0,0,2,2,4]
        [3, 9, 9, 3, 5, 7, 2],  # [0,0,0,3,3,3,6]
        [1, 5, 3, 6, 7, 6, 5]   # [0,0,2,0,0,5,6]
        ]

for case in cases:
    start = time.time()
    print(solution(case))
    end = time.time()
    msg = "the runtime for {func} took {time} seconds to complete"
    print(msg.format(
        func = solution.__name__,
        time = end - start
        ))

    start = time.time()
    print(solution2(case))
    end = time.time()
    print(msg.format(
        func = solution2.__name__,
        time = end - start
        ))
