# https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB

def rotateImage(a):
    n = len(a) - 1
    for i, row in enumerate(a[:-1]):
        for j, col in enumerate(row[i:-(i + 1)], i):
            a[i][j], a[n - j][i] = a[n - j][i], a[i][j]

            a[n - j][i], a[n - i][n - j] = a[n - i][n - j], a[n - j][i]

            a[n - i][n - j], a[j][n - i] = a[j][n - i], a[n - i][n - j]

    return a


cases = [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ],
        [
            [10,9,6,3,7],
            [6,10,2,9,7],
            [7,6,3,8,2],
            [8,9,7,9,9],
            [6,8,6,8,2]
            ],
        ]
for case in cases:
    print(rotateImage(case))
