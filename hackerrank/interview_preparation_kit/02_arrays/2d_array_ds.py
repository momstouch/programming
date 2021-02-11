# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def hourglassSum(arr):
    nrow = len(arr)
    ncol = len(arr[0])

    ans = -9 * 7
    c = 0
    for i in range(nrow - 2):
        for j in range(ncol - 2):
            ans = max(ans, arr[i][j] + arr[i][j+1] + arr[i][j+2] +\
                    arr[i+1][j+1] +\
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
    return ans

cases = [
        ([
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4 ,0]
            ], 19)
        ]
for arr, answer in cases:
    assert hourglassSum(arr) == answer
