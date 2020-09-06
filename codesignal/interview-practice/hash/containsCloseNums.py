# https://app.codesignal.com/interview-practice/task/njfXsvjRthFKmMwLC

def containsCloseNums_brute_force(nums, k):
    # brute-force, causing time out error
    for i in range(len(nums) - 1):
        jrange = i + k + 1 if i + k + 1 < len(nums) else len(nums)
        for j in range(i + 1, jrange):
            if nums[i] == nums[j]:
                return True

    return False


def containsCloseNums(nums, k):
    dic = {}
    for i in range(len(nums)):
        num = nums[i]

        if i > k:
            dic.pop(next(iter(dic)))

        dic[num] = dic.get(num, 0) + 1
        if dic[num] > 1:
            return True

    return False


def containsCloseNums_smarter(nums, k):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i

    return False


cases = [
        [[0, 1, 2, 3, 5, 2], 3],        # True
        [[0, 1, 2, 3, 5, 2], 2],        # False
        ]
for nums, k in cases:
    print(containsCloseNums(nums, k))
