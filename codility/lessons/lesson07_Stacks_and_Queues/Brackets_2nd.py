# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

def solution(S):
    stack = []

    for s in S:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        elif not stack:
            return 0
        else:
            ss = ord(stack.pop())
            s = ord(s)
            if ss + 1 != s and ss + 2 != s:
                return 0

    return 0 if stack else 1


cases = [
        ("{[()()]}", 1),
        ("([)()]", 0),
        ]
for s, gt in cases:
    assert solution(s) == gt
