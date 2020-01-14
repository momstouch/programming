

def solution(A, B):
    n = len(A)
    stack = [0]

    for q in range(1, n):

        while True:
            p = stack[-1] # read top

            if B[p] == 1 and B[q] == 0:
                if A[p] < A[q]:
                    stack.pop() # p is eaten

                    if len(stack) == 0:
                        stack.append(q)
                        break

                    p = stack[-1]
                else: # q is eaten
                    break
            else:
                stack.append(q)
                break

    # There are live fish in the stack
    return len(stack)


# clean code
def solution2(A, B):
    n = len(A)
    stack = [] # for downstream fishes

    n_ups_fish = 0

    for fish in range(n):
        if B[fish] == 1: # push downstream fishes to stack
            stack.append(fish)
        else:
            size = A[fish]
            while stack: # upstream fish is bigger
                if size > A[stack[-1]]:
                    stack.pop() # eaten
                else: # downstream fish is bigger
                    break
            if not stack:
                n_ups_fish += 1

    return len(stack) + n_ups_fish


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

print(solution2(A, B))
