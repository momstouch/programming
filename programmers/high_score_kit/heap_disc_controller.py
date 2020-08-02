# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    jobs = sorted(jobs, key=lambda x : x[0], reverse=False)
    idx = 0
    pq = []
    sums = 0
    end_of_curj = 0
    size = len(jobs)

    while idx < size or pq:

        for i in range(idx, size):
            if end_of_curj >= jobs[i][0]:
                heapq.heappush(pq, (jobs[i][1], jobs[i][0]))
                idx += 1
            else:
                break

        if pq:
            j_length, request = heapq.heappop(pq)
            sums += end_of_curj - request + j_length
            end_of_curj += j_length
        else:
            end_of_curj = jobs[i][0]

    return sums // size


cases = [
        [[0, 3], [1, 9], [2, 6]], # 9
        [[0, 3], [4, 3], [8, 3]], # 3
        [[0, 5], [6, 1], [6, 2]], # 3
        [[0, 5], [6, 2], [6, 1]], # 3
        [[0, 5], [2, 2], [5, 3]], # 5
        [[0, 5], [2, 2], [4, 2]], # 5
        ]
for c in cases:
    print(solution(c))
