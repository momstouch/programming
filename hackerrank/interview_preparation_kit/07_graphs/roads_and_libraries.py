# https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

def dfs(graph, visited, start):
    visited[start] = True

    ret = 1
    for v in graph[start]:
        if visited[v] is False:
            ret += dfs(graph, visited, v)
    return ret

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib

    graph = [[] for _ in range(n)]
    visited = [False] * len(graph)

    for i, j in cities:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)

    return sum((dfs(graph, visited, i) - 1) * c_road + c_lib for i in \
            range(n) if not visited[i])

cases = [
        (3, 2, 1, [[1,2],[3,1],[2,3]], 4),
        (6, 2, 5, [[1,3],[3,4],[2,4],[1,2],[2,3],[5,6]], 12),
        ]
for n, c_lib, c_road, cities, ans in cases:
    assert roadsAndLibraries(n, c_lib, c_road, cities) == ans
