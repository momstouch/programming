# https://leetcode.com/problems/two-sum/


class Solution:
    # Runtime: 44 ms
    # Memory Usage: 15.2 MB
    def twoSum(self, nums: list, target: int) -> list:
        # using hash
        table = {}
        for idx, n in enumerate(nums):
            table[n] = table.get(n, []) + [idx]

        answer = []
        for n in nums:
            if table.get(target - n, None) is not None:
                if target - n == n and len(table[n]) > 1:
                    return sorted(table[n])
                elif table[n] != table[target - n]:
                    return sorted(table[n] + table[target - n])


    # Runtime: 36 ms
    # Memory Usage: 14.3 MB
    # if some_key in dict is faster than dict.get(some_key)
    def twoSum_2(self, nums: list, target: int) -> list:
        table = {}
        for idx, n in enumerate(nums):
            to_target = target - n

            #if table.get(to_target, False) is not False:
            if to_target in table:
                return [table[to_target], idx]

            table[n] = idx


nums = [2, 7, 11, 15]
target = 9
# return [0, 1]

#nums = [3, 2, 4]
#target = 6

solution = Solution()
print(solution.twoSum(
    nums = nums,
    target = target))

print(solution.twoSum_2(
    nums = nums,
    target = target))
