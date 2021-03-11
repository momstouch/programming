# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

DX = [-1,0,1,0]
DY = [0,-1,0,1]

def dfs(i, j, depth):

T = int(input())
for case in range(1, T + 1):
    N, K = list(map(int, input().split(' ')))
    trail = [list(map(int, input().split(' '))) for _ in range(N)]
    visit = [[False for _ in range(N)] for _ in range(N)]

    _max = 0
    for row in trail:
        m = max(row)
        _max = max(m, _max)

    ans = 0
    for i in range(N):
        for j in range(N):
            if trail[i][j] == _max:
                ans = max(ans, dfs(i, j, 0))

    print("#%d" % (case), ans)
