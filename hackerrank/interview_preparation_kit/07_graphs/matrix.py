# https://www.hackerrank.com/challenges/matrix/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs&h_r=next-challenge&h_v=zen&page=2&h_r=next-challenge&h_v=zen

from collections import deque
def bfs(
        n,
        g, # graph
        adj,
        m, # machines
        start
        ):
    if not m:
        return 0

    que = deque([start])
    v = [-1] * n
    v[start] = 10 ** 6 + 1

    time = 0

    while que:
        i = que.popleft()

        for j in adj.get(i, []):
            if v[j] == -1:

                v[j] = min(v[i], g[i][j])
                que.append(j)

                if j in m:
                    m.remove(j)
                    time += v[j]
                    v[j] = 10 ** 6 + 1

    return time

def minTime(roads, machines):
    n = len(roads) + 1

    g = [[0 for _ in range(n)] for _ in range(n)]
    adj = {}
    for f, t, c in roads:
        g[f][t] = c
        g[t][f] = c
        adj[f] = adj.get(f, []) + [t]
        adj[t] = adj.get(t, []) + [f]

    ans = 0
    while machines:
        m = machines.pop(0)
        ans += bfs(n, g, adj, machines, m)
    
    print(ans)
    return ans

cases = [
        ([[2,1,8],[1,0,5],[2,4,5],[1,3,4]], [2,4,0], 10),
        ([[0,1,4],[1,2,3],[1,3,7],[0,4,2]], [2,3,4], 5),
        ]
for r, m, answer in cases:
    assert minTime(r, m) == answer

if __name__ == "__main__":
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    result = minTime(roads, machines)
    print(result) # 2746470
