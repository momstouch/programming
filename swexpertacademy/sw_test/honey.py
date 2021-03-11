# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AV5V4A46AdIDFAWu&categoryId=AV732SG66sEDFAW7&categoryType=BOX

from itertools import combinations
import heapq

T = int(input())
for case in range(1, T + 1):
    N, M, C = list(map(int, input().rstrip().split(' ')))
    beehive = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

    maxvals = []
    for i in range(N):
        for j in range(N - M + 1):
            max_val = 0
            for k in range(1, M + 1):
                for s in combinations(beehive[i][j: j + M], k):
                    if sum(s) <= C:
                        max_val = max(max_val, sum(map(lambda x: x ** 2, s)))
            heapq.heappush(maxvals, (-max_val, i, j))

    ans, i1, j1 = heapq.heappop(maxvals) 
    while maxvals:
        val, i2, j2 = heapq.heappop(maxvals)
        if i1 == i2 and j1+M > j2:
            continue
        ans += val
        break
    
    print("#%d" % (case), ans * -1)
