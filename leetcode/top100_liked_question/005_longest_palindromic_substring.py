# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    # Runtime: 524 ms
    # Memory Usage: 12.8 MB
    def f(self, s: str, left: int, right: int):
        if left >= 0 and right < len(s):
            if s[left] == s[right]:
                if self.max_len < right - left + 1:
                    self.max_len = right - left + 1
                    self.result = [left, right]
                self.f(s, left - 1, right + 1)


    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        self.max_len = 1
        self.result = [0, 0]
        for i in range(len(s)):
            self.f(s, i, i + 1)
            self.f(s, i, i + 2)

        return s[self.result[0]: self.result[1] + 1]


testcase = [
        "babad",        # "bab" or "aba"
        "cbbd",         # "bb"
        ]

s = Solution()
for t in testcase:
    print(s.longestPalindrome(t))
