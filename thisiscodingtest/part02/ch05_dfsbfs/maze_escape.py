
from collections import deque

def bfs(graph):
    que = deque([(0, 0)])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        vi, vj = que.popleft()

        for i, j in zip(dx, dy):
            ni = vi + i
            nj = vj + j

            if ni < 0 or ni >= len(graph) or nj < 0 or nj >= len(graph[0]):
                continue
            if graph[ni][nj] == 0:
                continue

            if graph[ni][nj] == 1:
                graph[ni][nj] = graph[vi][vj] + 1
                que.append((ni, nj))

    return graph[-1][-1]
        

def solution(maze):
    graph = [[1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "0":
                graph[i][j] = 0

    return bfs(graph)

maze = [
        "101010",
        "111111",
        "000001",
        "111111",
        "111111"
        ]
assert solution(maze) == 10
