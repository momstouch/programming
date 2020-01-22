# https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    # Runtime: 148 ms
    # Memory Usage: 12.6 MB
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        n_total = len(nums1) + len(nums2)
        target_idx = n_total // 2

        combine = []
        while nums1 and nums2:
            n1 = nums1[0]
            n2 = nums2[0]

            combine.append(nums1.pop(0) if n1 < n2 else nums2.pop(0))

        combine.extend(nums1 if nums1 else nums2)

        if n_total % 2: # odd
            return float(combine[target_idx])
        else: # even
            return (combine[target_idx - 1] + combine[target_idx]) / 2.0


    # Runtime: 80 ms
    # Memory Usage: 12.9 MB
    def findMedianSortedArrays2(self, nums1: list, nums2: list) -> float:
        combine = nums1 + nums2
        combine.sort()
        length = len(combine)
        target_idx = length // 2

        if length % 2: # odd
            return float(combine[target_idx])
        else: # even
            return (combine[target_idx - 1] + combine[target_idx]) / 2.0


testcases = [
        [[1, 3], [2]],      # 2.0
        [[1, 2], [3, 4]],   # 2.5
        ]

s = Solution()
for nums1, nums2 in testcases:
    print(s.findMedianSortedArrays2(nums1, nums2))
    print(s.findMedianSortedArrays(nums1, nums2))
