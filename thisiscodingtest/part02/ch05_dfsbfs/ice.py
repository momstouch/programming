
def dfs(graph, x, y, visited):
    if x >= len(graph) or y >= len(graph[x]) or graph[x][y] == "1" or visited[x][y]:
        return 0

    visited[x][y] = True
    dfs(graph, x+1, y, visited)
    dfs(graph, x, y+1, visited)
    return 1

def solution(graph):
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    ans = 0

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            ans += dfs(graph, i, j, visited)

    return ans
    

cases = [
        (["00110", "00011", "11111", "00000"], 3),
        (["001", "010", "101"], 3),
        ]
for graph, answer in cases:
    assert solution(graph) == answer
