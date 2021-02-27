# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs&h_r=next-challenge&h_v=zen

from collections import deque
def bfs(graph, visited, ids, val):
    try:
        start = ids.index(val)
    except ValueError:
        return -1

    que = deque([start])
    visited[start] = 1

    ans = len(visited)

    while que:
        i = que.popleft()

        for j in graph.get(i, []):
            if visited[j] == 0:
                if ids[j] == val:
                    ans = min(ans, visited[i])
                    visited[j] = 1
                else:
                    visited[j] = visited[i] + 1
                que.append(j)

    return -1 if ans == len(visited) else ans

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = {}
    for f, t in zip(graph_from, graph_to):
        graph[f-1] = graph.get(f-1, []) + [t-1]
        graph[t-1] = graph.get(t-1, []) + [f-1]

    visited = [0] * graph_nodes

    return bfs(graph, visited, ids, val)

cases = [
        (4, [1,1,4], [2,3,2], [1,2,1,1], 1, 1),
        (4, [1,1,4], [2,3,2], [1,2,3,4], 2, -1),
        (5, [1,1,2,3], [2,3,4,5], [1,2,3,3,2], 2, 3),
        ]
for gnodes, gfrom, gto, ids, val, ans in cases:
    assert findShortest(gnodes, gfrom, gto, ids, val) == ans
