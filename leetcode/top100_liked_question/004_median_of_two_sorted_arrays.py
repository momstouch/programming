# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        one_nums = []
        while nums1 or nums2:
            pass


testcases = [
        [[1, 3], [2]],      # 2.0
        [[1, 2], [3, 4]],   # 2.5
        ]

s = Solution()
for nums1, nums2 in testcases:
    print(s.findMedianSortedArrays(nums1, nums2))
