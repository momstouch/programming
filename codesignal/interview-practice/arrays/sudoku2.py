# https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn
from collections import Counter

def sudoku2(grid):

    for i in range(len(grid)):

        row = Counter(grid[i])
        row.pop('.', None)
        if sum(row.values()) != len(row):
            return False
        col = Counter([row[i] for row in grid if row[i] != '.'])
        if sum(col.values()) != len(col):
            return False

        subgrid = []
        for j in range(i // 3 * 3, i // 3 * 3 + 3):
            for k in range(i * 3 % 9, i * 3 % 9 + 3):
                if grid[j][k] != '.':
                    subgrid.append(grid[j][k])

        subgrid = Counter(subgrid)
        if sum(subgrid.values()) != len(subgrid):
            return False

    return True


cases = [
        [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']],
        [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
        ]
for case in cases:
    print(sudoku2(case))
