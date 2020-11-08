# https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

def solution(S):
    stack = []

    for s in S:
        if s == '(':
            stack.append(s)
        elif not stack:
            return 0
        else:
            stack.pop()

    return 0 if stack else 1


cases = [
        ("(()(())())", 1),
        ("())", 0),
        ]
for s, gt in cases:
    assert solution(s) == gt
