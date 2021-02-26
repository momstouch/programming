
def dfs(graph, v, visited):
    print(v, end = ' ')

    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)

graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
        ]
visited = [False] * len(graph)
dfs(graph, 1, visited)
