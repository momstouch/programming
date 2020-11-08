# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/

def solution(H):
    stack = []
    blk = 0
    
    for h in H:
        if not stack:
            stack.append(h)
        else:
            if stack[-1] < h:
                stack.append(h)
            elif stack[-1] > h:
                while stack and stack[-1] > h:
                    stack.pop()
                    blk += 1
                if not stack or stack[-1] != h:
                    stack.append(h)

    return blk + len(stack)


cases = [
        ([8,8,5,7,9,8,7,4,8], 7),
        ]
for h, gt in cases:
    assert solution(h) == gt
