# https://programmers.co.kr/learn/courses/30/lessons/17679

from collections import Counter

def solution(m, n, board):
    score = [[False] * n for _ in range(m)]
    board = [list(row) for row in board]

    while True:
        flag = False
        for i in range(m - 1):
            for j in range(n - 1):

                if len(Counter(board[i][j:j + 2] + board[i + 1][j:j + 2])) == 1:
                    score[i][j], score[i][j + 1] = True, True
                    score[i + 1][j], score[i + 1][j + 1] = True, True

        for i in range(m - 1, 0, -1):
            for j in range(n):
                if score[i][j]:
                    ii = i - 1
                    while ii >= 0 and score[ii][j]:
                        board[ii][j] = '*'
                        ii -= 1
                    if ii >= 0:
                        score[ii][j] = True
                        score[i][j] = False
                        board[i][j] = board[ii][j]
                        board[ii][j] = '*'
                        flag = True

        if not flag:
            break

    return sum([sum(s) for s in score])

cases = [
        (6, 6, ["IIIIOO", "IIIOOO", "IIIOOI", "IOOIII", "OOOIII", "OOIIII"],32),
        (6,2, ["AA", "AA", "CC", "AA", "AA", "DD"],8),
        (8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"],8),
        (6,2, ["DD", "CC", "AA", "AA", "CC", "DD"],12),
        (4,2, ["CC", "AA", "AA", "CC"],8),
        (3,2,["AA","AA","AB"],4),
        (2,2,["AA","AB"],0),
        (2,2,["AA","AA"],4),
        (4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"],14),
        (6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"],15),
        (6,6,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE"],32),
        (5,6,["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"],24),
        (6,6,["AABBEE", "AAAEEE", "VAAEEV", "AABBEE", "AACCEE", "VVCCEE"],32),
        ]
for m, n, board, ans in cases:
    assert solution(m, n, board) == ans
