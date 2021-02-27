# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs&h_r=next-challenge&h_v=zen&page=2

def dfs(grid, visited, x, y):
    if x < 0 or x >= len(grid) or y < 0 or \
            y >= len(grid[0]) or visited[x][y] or \
            grid[x][y] == 0:
        return 0

    visited[x][y] = True
    return 1 + dfs(grid, visited, x+1, y) + dfs(grid, visited, x-1, y) +\
            dfs(grid, visited, x, y+1) + dfs(grid, visited, x, y-1) +\
            dfs(grid, visited, x-1, y+1) + dfs(grid, visited, x+1, y+1) +\
            dfs(grid, visited, x+1, y-1) + dfs(grid, visited, x-1, y-1)

def maxRegion(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    region = -1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0 and not visited[i][j]:
                region = max(dfs(grid, visited, i, j), region)

    return region

cases = [
        ([[1,1,0,0],[0,1,1,0],[0,0,1,0],[1,0,0,0]], 5),
        ]
for grid, answer in cases:
    assert maxRegion(grid) == answer
