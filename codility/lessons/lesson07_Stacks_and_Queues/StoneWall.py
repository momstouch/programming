# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/


def solution(H):
    stack = []
    blocks = 0

    for h in H:
        if not stack:
            stack.append(h)

        elif stack[-1] > h:
            while stack and stack[-1] > h:
                stack.pop()
                blocks += 1
            if not stack or stack[-1] < h:
                stack.append(h)

        elif stack[-1] < h:
            stack.append(h)

    return blocks + len(stack)


H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))
