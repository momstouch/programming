# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

TUNNEL = [
        [0], # dummy
        [(-1,0),(0,1),(0,-1),(1,0)],
        [(-1,0),(1,0)],
        [(0,-1),(0,1)],
        [(-1,0),(0,1)],
        [(0,1),(1,0)],
        [(0,-1),(1,0)],
        [(-1,0),(0,-1)],
        ]

from collections import deque
def bfs(N, M, graph, startx, starty, depth):
    que = deque([(startx, starty)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[startx][starty] = 1

    while que:
        x, y = que.popleft()
        moves = TUNNEL[graph[x][y]]

        for dx, dy in moves:
            xx = x + dx
            yy = y + dy
            if xx >= 0 and xx < N and yy >= 0 and yy < M:
                if graph[xx][yy] == 0 or visited[xx][yy] != 0:
                    continue
                for ddx, ddy in TUNNEL[graph[xx][yy]]:
                    if xx + ddx == x and yy + ddy == y:
                        visited[xx][yy] = visited[x][y] + 1
                        que.append((xx, yy))
                        break

    return sum([1 for rows in visited for v in rows if v >= 1 and v <= depth])

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = list(map(int, input().rstrip().split(' ')))
    tnl = []
    for _ in range(N):
        tnl.append(list(map(int, input().rstrip().split(' '))))

    print("#%d" % test_case, bfs(N, M, tnl, R, C, L))
