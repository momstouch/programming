

# O(N) solution
def solution(S):
    stack = []
    size = len(S)

    for idx in range(size):
        c = S[idx]
        if c == ']' or c == '}' or c == ')':
            if len(stack) != 0:
                left = stack.pop()
                if left != chr(ord(c) - 1) and left != chr(ord(c) - 2):
                    return 0
            else:
                return 0
        else:
            stack.append(c) # push to stack

    if len(stack) == 0:
        return 1
    return 0


S = "{[()()]}" # positive
S = "([)()]" # negative
print(solution(S))
