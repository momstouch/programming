# https://app.codesignal.com/interview-practice/task/BG94ZFECSNo6Kv7XW/description

def kthLargestElement_qsort_time_exceeded(nums, k):
    def qsort(n, start, end, k, rev):
        if k <= start or start >= end:
            return

        pivot = n[start]
        left = start + 1
        right = end

        while left <= right:
            while left <= end and (n[left] >= pivot if rev else n[left] <= pivot):
                left += 1
            while right > start and (n[right] <= pivot if rev else n[right] >= pivot):
                right -= 1

            if left > right:
                n[start], n[right] = n[right], n[start]
            else:
                n[left], n[right] = n[right], n[left]

        qsort(n, start, right - 1, k, rev)
        qsort(n, right + 1, end, k, rev)

    rev = False
    if k < len(nums) // 2:
        rev = True
    qsort(nums, 0, len(nums) - 1, k, rev)

    return nums[k - 1] if rev else nums[-k]


import heapq

def kthLargestElement_notmysolution(nums, k):
    hq = []
    for i, n in enumerate(nums):
        if i < k:
            heapq.heappush(hq, n)
        elif hq[0] < n:
            heapq.heappushpop(hq, n)

    return hq[0]


def kthLargestElement(nums, k):
    def partition(arr, b, e):
        p = arr[b]
        l = b + 1
        r = e

        while l <= r:
            while l <= e and arr[l] >= p:
                l += 1
            while r > b and arr[r] <= p:
                r -= 1

            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
        arr[b], arr[r] = arr[r], arr[b]
        return r

    def qsort(arr, b, e, k):
        p = partition(arr, b, e)
        if p == k:
            return arr[p]
        if b <= k and p > k:
            return qsort(arr, b, p - 1, k)
        if p < k and e >= k:
            return qsort(arr, p + 1, e, k)

    return qsort(nums, 0, len(nums) - 1, k - 1)


cases = [
        ([7, 6, 5, 4, 3, 2, 1], 2), # 6
        ([99, 99], 1),  # 99
        ([-1, 2, 0], 2),    # 0
        ([3, 1, 2, 4], 2),  # 3
        ]
for nums, k in cases:
    print(kthLargestElement(nums, k))
