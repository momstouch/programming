# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AV597vbqAH0DFAVl&categoryId=AV732SG66sEDFAW7&categoryType=BOX

from functools import partial

dxy = ([0,0],[-1,0],[1,0],[0,-1],[0,1])

ACT = 0
X = 1
Y = 2
POP = 3
DIR = 4

def is_deadzone(x, y, n):
    if x == 0 or x == n - 1 or y == 0 or y == n - 1:
        return True
    return False

def turnback(direction):
    if direction == 1: return 2
    if direction == 2: return 1
    if direction == 3: return 4
    if direction == 4: return 3

T = int(input())
for case in range(1, T + 1):
    N, M, K = list(map(int, input().rstrip().split(' ')))
    micro = [[True] + list(map(int, input().rstrip().split(' '))) for _ in range(K)]
    # [active, x, y, population, direction]
    grid = [[[] for _ in range(N)] for _ in range(N)]
    is_dead = partial(is_deadzone, n = N)

    t = 0

    while t < M:

        for i, m in enumerate(micro):
            if not m[ACT]: # merged into others or died out
                continue

            x, y = m[X], m[Y]
            grid[x][y] = []

            # move
            dx, dy = dxy[m[DIR]]
            m[X] += dx
            m[Y] += dy
            if is_dead(m[X], m[Y]): # is on the red line
                m[DIR] = turnback(m[DIR])
                m[POP] = m[POP] // 2
                if m[POP] == 0: # die out
                    m[ACT] = False
                    continue
        # end of for i, m in enumerate(micro):

        # union
        for i, m in enumerate(micro):
            if not m[ACT]:
                continue
            grid[m[X]][m[Y]].append(i)

        for i in range(N):
            for j in range(N):
                if len(grid[i][j]) > 1:
                    fight = [micro[g][POP] for g in grid[i][j]]
                    winner = fight.index(max(fight))
                    winner = grid[i][j][winner]
                    micro[winner][POP] = sum(fight)
                    for g in grid[i][j]:
                        if g != winner:
                            micro[g][ACT] = False
        t += 1
    # end of while t < M:
    result = sum([m[POP] for m in micro if m[ACT]])
    print("#%d" % (case), result)

# end of for t in range(1, T + 1):
