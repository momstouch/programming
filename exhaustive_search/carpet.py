# https://programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, red):
    volume = brown + red

    for hor in range(volume - 1, 2, -1):
        if volume % hor == 0:
            ver = volume // hor

            if (hor - 2) * (ver - 2) == red:
                return [hor, ver]


testcase = [
        [10, 2], # ret [4, 3]
        [8, 1],  # ret [3, 3]
        [24, 24] # ret [8, 6]
        ]

for b, r in testcase:
    print(solution(b, r))
