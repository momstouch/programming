# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def minimumSwaps(arr):
    ans = 0
    brr = [i for i, a in sorted(enumerate(arr), key = lambda x: x[1])]

    for i in range(len(arr)):
        if i != arr[i] - 1:
            ans += 1
            swapped = arr[i] - 1
            arr[i], arr[brr[i]] = arr[brr[i]], arr[i]
            brr[swapped] = brr[i]

    return ans

cases = [
        ([4, 3, 1, 2], 3),
        ([2,3,4,1,5], 3),
        ([1,3,5,2,4,6,7], 3),
        ]
for arr, answer in cases:
    print(arr)
    assert minimumSwaps(arr) == answer
