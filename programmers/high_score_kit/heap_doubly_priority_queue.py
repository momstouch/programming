# https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq


def solution(operations):
    minq = []
    maxq = []
    deleted = []

    for idx, opstring in enumerate(operations):
        op, num = opstring.split(' ')
        num = int(num)

        if op == "I":
            heapq.heappush(minq, (num, idx))
            heapq.heappush(maxq, (-num, idx))
        else:
            if num > 0: # pop max
                n, i = heapq.heappop(maxq)
            else:
                n, i = heapq.heappop(minq)

            deleted.append(i)

    answer = [0, 0]

    if minq and maxq:
        while True:
            n, i = heapq.heappop(maxq)
            if i not in deleted:
                answer[0] = -n
                break
        while True:
            n, i = heapq.heappop(minq)
            if i not in deleted:
                answer[1] = n
                break

    return answer


cases = [
        ["I 16","D 1"],              # 	[0,0]
        ["I 7","I 5","I -5","D -1"], #	[7,5]
        ]
for case in cases:
    print(solution(case))
