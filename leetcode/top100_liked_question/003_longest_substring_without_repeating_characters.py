# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    # Runtime: 52 ms
    # Memory Usage: 13 MB
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        queue = []
        longest = 0
        for ch in s:
            if not ch in queue:
                queue.append(ch)
            else:
                longest = max(len(queue), longest)
                while queue.pop(0) != ch:
                    pass
                queue.append(ch)

        return max(longest, len(queue))


testcase = [
        "abcabcbb", # 3
        "bbbbb",    # 1
        "pwwkew",   # 3
        "aab",      # 2
        "dvdf",     # 3
        "ckilbkd",  # 5
        "ohvhjdml", # 6
        ]

solution = Solution()
for test in testcase:
    print(solution.lengthOfLongestSubstring(s = test))
