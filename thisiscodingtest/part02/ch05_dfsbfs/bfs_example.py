
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end = ' ')

        adj = sorted(graph[v])
        for i in adj:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
        ]
visited = [False] * len(graph)
bfs(graph, 1, visited)
