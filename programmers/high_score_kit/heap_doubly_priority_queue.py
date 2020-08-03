# https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq
import time


def solution(operations):
    minq = []
    maxq = []
    table = {}

    for idx, opstring in enumerate(operations):
        op, num = opstring.split(' ')
        num = int(num)

        if op == "I":
            heapq.heappush(minq, (num, idx))
            heapq.heappush(maxq, (-num, idx))
            table[idx] = True
        elif table:
            if num > 0: # pop max
                n, i = heapq.heappop(maxq)
                n = -n
            else:
                n, i = heapq.heappop(minq)

            del table[i]

    answer = [0, 0]

    if minq and maxq:
        while maxq:
            n, i = heapq.heappop(maxq)
            if table.get(i, False):
                answer[0] = -n
                break
        while minq:
            n, i = heapq.heappop(minq)
            if table.get(i, False):
                answer[1] = n
                break

    return answer


def better_solution(operations):
    heap = []

    for operation in operations:
        op, num = operation.split(' ')
        num = int(num)

        if op == "I":
            heapq.heappush(heap, num)
        elif heap:
            if num < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]


cases = [
        ["I 16","D 1"],              # 	[0,0]
        ["I 7","I 5","I -5","D -1"], #	[7,5]
        ]
t0 = time.time()
for case in cases:
    print(solution(case))
print("%.6f" % (time.time() - t0))

t0 = time.time()
for case in cases:
    print(better_solution(case))
print("%.6f" % (time.time() - t0))
