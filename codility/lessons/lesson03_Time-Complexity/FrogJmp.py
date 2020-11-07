# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    return ((Y - X) // D) + (1 if (Y - X) % D else 0)


cases = [
        (10, 85, 30, 3),
        ]
for x, y, d, gt in cases:
    assert solution(x, y, d) == gt
