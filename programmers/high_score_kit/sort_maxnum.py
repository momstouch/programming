# https://programmers.co.kr/learn/courses/30/lessons/42746
import time


def solution(numbers):
    return ''.join(
            sorted(
                map(str, numbers),
                reverse = True,
                key = lambda x: x * 3
                )
            )

def solution2(numbers):
    return str(int(''.join(
            sorted(
                map(str, numbers),
                reverse = True,
                key = lambda x: x * 3
                )
            )))



cases = [
        [6, 10, 2],         # "6210"
        [3, 30, 34, 5, 9],  # "9534330"
        [0, 0, 0, 0]
        ]
t0 = time.time()
for case in cases:
    print(solution(case))
print("running time %.6f" % (time.time() - t0))

t0 = time.time()
for case in cases:
    print(solution2(case))
print("running time %.6f" % (time.time() - t0))
