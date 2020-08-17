# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for hori in range(yellow, 0, -1):
        if yellow % hori == 0:
            vert = yellow // hori
            want_n_b = vert * 2 + hori * 2 + 4
            if brown == want_n_b:
                return [hori + 2, vert + 2]

    return None


def solution2(brown, yellow):
    volume = brown + yellow

    for hor in range(volume - 1, 2, -1):
        if volume % hor == 0:
            ver = volume // hor

            if (hor - 2) * (ver - 2) == yellow:
                return [hor, ver]


cases = [
        [10, 2],    # [4, 3]
        [8, 1],     # [3, 3]
        [24, 24],   # [8, 6]
        ]
for brown, yellow in cases:
    print(solution(brown, yellow))
