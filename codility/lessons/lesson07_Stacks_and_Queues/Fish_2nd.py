# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

def solution2(A, B):
    stack = []

    for i, (a, b) in enumerate(zip(A, B)):
        if not stack:
            stack.append((a, b))
        elif stack[-1][1] == 1 and b == 0:
            while stack:
                if stack[-1][1] == 1 and stack[-1][0] < a:
                    stack.pop()
                else:
                    break
            if not stack or stack[-1][1] == 0:
                stack.append((a, b))
        else:
            stack.append((a, b))

    return len(stack)


def solution(A, B):
    stack = []
    ans = 0

    for a, b in zip(A, B):
        if b == 1:
            stack.append(a)
        else:
            while stack:
                if stack[-1] < a:
                    stack.pop()
                else:
                    break
            if not stack:
                ans += 1

    return ans + len(stack)


cases = [
        (([4,3,2,1,5], [0,1,0,0,0]), 2),
        (([4,3,2,1,5], [1,1,0,0,0]), 1),
        ]
for (a, b), gt in cases:
    assert solution(a, b) == gt
