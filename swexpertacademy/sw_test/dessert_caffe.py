# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(graph, desert, x, y, direct, endx, endy, ans):
    xx = x + dx[direct]
    yy = y + dy[direct]

    if xx >= len(graph) or xx < 0 or yy >= len(graph) or yy < 0:
        return 
    if xx == endx and yy == endy:
        ans.append(desert[graph[x][y]])
        return 
    if desert[graph[xx][yy]] != 0:
        return 

    desert[graph[xx][yy]] = desert[graph[x][y]] + 1
    dfs(graph, desert, xx, yy, direct, endx, endy, ans)
    if direct + 1 < len(dx):
        dfs(graph, desert, xx, yy, direct + 1, endx, endy, ans)
    desert[graph[xx][yy]] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    desert = [0] * 101
    ans = [-1]
    
    for i in range(N):
        for j in range(1, N-1):
            desert[cafe[i][j]] = 1
            dfs(cafe, desert, i, j, 0, i, j, ans)
            desert[cafe[i][j]] = 0

    print("#%d" % (t), max(ans))
