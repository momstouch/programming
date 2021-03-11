# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

from collections import deque
def get_total_fee(k):
    return k * k + (k - 1) * (k - 1)

def bfs(n, m, city):
    n_house = sum([c for r in city for c in r])

    max_house_covered = 0

    for i in range(n):
        for j in range(n):

            visit = [[0 for _ in range(n)] for _ in range(n)]
            visit[i][j] = 1
            cur_k = 1
            n_house_covered = 0

            que = deque([(i, j)])
            while que:
                x, y = que.popleft()

                if visit[x][y] > cur_k:
                    fee = get_total_fee(cur_k) 
                    if fee <= n_house_covered * m:
                        max_house_covered = max(max_house_covered, n_house_covered)
                    if cur_k > n + 2:
                        break
                    cur_k = visit[x][y]

                n_house_covered += city[x][y]

                if x - 1 >= 0 and visit[x - 1][y] == 0: # top
                    que.append((x - 1, y))
                    visit[x - 1][y] = visit[x][y] + 1
                if y - 1 >= 0 and visit[x][y - 1] == 0: # left
                    que.append((x, y - 1))
                    visit[x][y - 1] = visit[x][y] + 1
                if y + 1 < n and visit[x][y + 1] == 0: # right
                    que.append((x, y + 1))
                    visit[x][y + 1] = visit[x][y] + 1
                if x + 1 < n and visit[x + 1][y] == 0: # bottom
                    que.append((x + 1, y))
                    visit[x + 1][y] = visit[x][y] + 1

                if not que and get_total_fee(cur_k) <= n_house_covered * m:
                    max_house_covered = max(max_house_covered, n_house_covered)

    return max_house_covered

T = int(input())
for case in range(1, T + 1):
    N, M = list(map(int, input().rstrip().split(' ')))
    city = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    #if case != 10: continue
    print("#%d" % (case), bfs(N, M, city))
