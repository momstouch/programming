# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import copy

DX = [-1,0,1,0]
DY = [0,-1,0,1]

def dfs(i, j, depth, dig, ans):
    go_deeper = True
    for di, dj in zip(DX, DY):
        ni = i + di
        nj = j + dj

        if ni >= 0 and ni < N and nj >= 0 and nj < N and\
                not visit[ni][nj]:
            if graph[i][j] > graph[ni][nj]:
                visit[ni][nj] = True
                dfs(ni, nj, depth + 1, dig, ans)
                visit[ni][nj] = False
            elif graph[i][j] <= graph[ni][nj] and not dig and \
                    graph[ni][nj] - K < graph[i][j]:
                graph[ni][nj] = graph[i][j] - 1
                visit[ni][nj] = True
                dfs(ni, nj, depth + 1, True, ans)
                graph[ni][nj] = origin[ni][nj]
                visit[ni][nj] = False
            else:
                go_deeper = False

    if not go_deeper:
        ans[0] = max(ans[0], depth)


T = int(input())
for case in range(1, T + 1):
    N, K = list(map(int, input().split(' ')))
    graph = [list(map(int, input().split(' '))) for _ in range(N)]
    origin = copy.deepcopy(graph)
    visit = [[False for _ in range(N)] for _ in range(N)]

    _max = 0
    for row in graph:
        m = max(row)
        _max = max(m, _max)

    ans = [0]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == _max:
                visit[i][j] = True
                dfs(i, j, 1, False, ans)
                visit[i][j] = False

    print("#%d" % (case), ans[0])
