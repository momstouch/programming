# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    i = 0
    stack = []

    while i < len(dartResult):
        dr = dartResult[i]

        if dr.isdigit():
            val = int(dr)
            if dartResult[i + 1].isdigit():
                val = int(dartResult[i: i + 2])
                i += 1
            stack.append(val)
        elif dr == "D":
            stack[-1] *= stack[-1]
        elif dr == "T":
            stack[-1] *= stack[-1] * stack[-1]
        elif dr == "*":
            stack[-2:] = [s * 2 for s in stack[-2:]]
        elif dr == "#":
            stack[-1] = stack[-1] * -1

        i += 1
    return sum(stack)

cases = [
        ("1S2D*3T", 37),
        ("1D2S#10S", 9),
        ("1D2S0T", 3),
        ("1S*2T*3S", 23),
        ("1D2S3T*", 59),
        ]
for dartresult, ans in cases:
    assert solution(dartresult) == ans
