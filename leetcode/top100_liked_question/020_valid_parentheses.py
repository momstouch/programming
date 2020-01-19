# https://leetcode.com/problems/valid-parentheses/


class Solution:
    # Runtime: 32 ms
    # Memory Usage: 12.8 MB
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch =='[':
                stack.append(ch)
            else:
                if not stack:
                    return False

                left = stack.pop()

                if left == '(' and (ch == '}' or ch == ']'):
                    return False
                elif left == '{' and (ch == ')' or ch == ']'):
                    return False
                elif left == '[' and (ch == '}' or ch == ')'):
                    return False

        if stack:
            return False
        return True


    # Runtime: 20 ms
    # Memory Usage: 12.7 MB
    def isValid2(self, s: str) -> bool:
        stack = []
        paren = {'(':')', '{':'}', '[':']'}

        for ch in s:
            if ch in paren:
                stack.append(ch)
            elif stack:
                left = stack.pop()
                if paren[left] != ch:
                    return False
            else:
                return False

        if not stack:
            return True
        return False


testcases = [
        "()",       # true
        "()[]{}",   # true
        "(]",       # false
        "([)]",     # false
        "{[]}",     # true
        ]
s = Solution()
for t in testcases:
    print(s.isValid2(t))
