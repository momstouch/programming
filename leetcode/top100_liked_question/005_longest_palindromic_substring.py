# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        


testcase = [
        "babad",        # "bab" or "aba"
        "cbbd",         # "bb"
        ]

s = Solution()
for t in testcase:
    print(s.longestPalindrome(t))
