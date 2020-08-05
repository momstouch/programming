# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    memo = [[0] * n] * n
    counter = [1]

    def bfs(n, computers, i, j):
        if memo[i][j] != 0:
            counter[0] += 1
            return

        memo[i][j] = counter[0]

        for ii in range(i, n):
            for jj in range(j, n):
                if computers[ii][jj] == 1 and ii != jj:
                    bfs(n, computers, jj, ii)

    bfs(n, computers, 0, 0)
    print(memo)

    return max(memo)


cases = [
        [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], # 2
        [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]], # 1
        ]
for n, computers in cases:
    print(solution(n, computers))
