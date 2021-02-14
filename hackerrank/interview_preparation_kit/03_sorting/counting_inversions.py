# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# merge sort: Counting Inversions
# cannot pass all cases using python3
def merge_sort(arr):
    temp = [0] * len(arr)

    def sort(low, high):

        inversions = 0

        if high - low >= 2:
            mid = (low + high) // 2
            inversions += sort(low, mid)
            inversions += sort(mid, high)
            inversions += merge(low, mid, high)

        return inversions

    def merge(low, mid, high):
        l, h = low, mid
        k = 0
        inversions = 0

        while l < mid and h < high:
            if arr[l] <= arr[h]:
                temp[k] = arr[l]
                k += 1
                l += 1
            else: # inversions
                temp[k] = arr[h]
                k += 1
                h += 1
                inversions += mid - l

        while l < mid:
            temp[k] = arr[l]
            k += 1
            l += 1
        while h < high:
            temp[k] = arr[h]
            k += 1
            h += 1

        for k, i in enumerate(range(low, high)):
            arr[i] = temp[k]

        return inversions

    return sort(0, len(arr))


# can pass all cases using python3
def inversions(arr):
    n = len(arr)
    if n == 1:
        return 0

    n1 = n // 2
    n2 = n - n1
    left = arr[:n1]
    right = arr[n1:]

    ans = inversions(left) + inversions(right)

    l = r = 0
    for i in range(n):
        if l < n1 and (r >= n2 or left[l] <= right[r]):
            arr[i] = left[l]
            ans += r # the number of elements in right before left elements
            l += 1
        elif r < n2:
            arr[i] = right[r]
            r += 1
    return ans

def countInversions(arr):
    return inversions(arr)
    #return merge_sort(arr)

cases = [
        ([1,1,1,2,2], 0),
        ([2,1,3,1,2], 4),
        ]
for arr, answer in cases:
    assert countInversions(arr) == answer
