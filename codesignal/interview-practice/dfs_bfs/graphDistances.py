# https://app.codesignal.com/interview-practice/task/QTirmApTj7sWaidLk

import sys
import heapq

def graphDistances(g, s):

    dist = [sys.maxsize] * len(g)
    dist[s] = 0

    que = []
    heapq.heappush(que, (dist[s], s))
    
    while que:
        _, u = heapq.heappop(que)

        for v, d in enumerate(g[u]):
            if d >= 0:
                alt = dist[u] + d
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(que, (dist[v], v))

    return dist


cases = [
        [
            [
                [-1, 3, 2],
                [2, -1, 0],
                [-1, 0, -1]
                ], 0
            ],  # [0, 2, 2]
        [
            [
                [-1,5,2,15],
                [2,-1,0,3],
                [1,-1,-1,9],
                [0,0,0,-1]
                ], 2
            ],  # [1, 6, 0, 9]
        [
            [
                [-1,3,2,-1],
                [3,-1,-1,1],
                [2,-1,-1,3],
                [-1,1,3,-1]
                ], 3
            ]
        ]
for g, s in cases:
    print(graphDistances(g, s))
