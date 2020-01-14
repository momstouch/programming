

# O(N)
def solution(S):
    stack = []

    for s in S:
        if s == '(': # stack only can have left
            stack.append(s) # push
        else:
            if not stack: # if stack is empty
                return 0
            stack.pop()

    if stack:
        return 0
    return 1


S = "(()(())())"
S = "())" # negative example
print(solution(S))
