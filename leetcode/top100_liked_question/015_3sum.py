

class Solution:
    def threeSum(self, nums: list) -> list:
        n = nums.copy()
        n.sort(reverse=True)

        ans = set()

        for i, v1 in enumerate(n[:-2], 0):
            for j, v2 in enumerate(n[i + 1:-1], i + 1):
                v12 = v1 + v2
                for v3 in n[j + 1:]:
                    if v3 > v12:
                        break
                    elif v12 + v3 == 0:
                        ans.add((v1, v2, v3))
                        break

        return [list(a) for a in ans]


nums = [
        [-1, 0, 1, 2, -1, -4],
        [0, 0, 0, 0]
        ]
s = Solution()

for num in nums:
    print(s.threeSum(num))
