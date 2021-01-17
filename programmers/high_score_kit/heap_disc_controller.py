# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    jobs = sorted(jobs, key=lambda x : x[0], reverse=False)
    answer = 0
    qu = [] # min heap
    t = 0 # current time
    i = 0 # index for jobs

    while i < len(jobs) or qu:
        if not qu and i < len(jobs):
            t = jobs[i][0]
        elif qu:
            length, request = heapq.heappop(qu)
            answer += t - request + length
            t += length

        while i < len(jobs) and t >= jobs[i][0]:
            request, length = jobs[i]
            heapq.heappush(qu, (length, request))
            i += 1

    return answer // len(jobs)


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
