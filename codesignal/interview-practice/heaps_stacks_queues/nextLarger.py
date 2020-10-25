# https://app.codesignal.com/interview-practice/task/MdHZFgZFERPPagfdD/description

# brute force algorithm but passed all tests
def nextLarger_bruteforce(a):
    ans = [-1] * len(a)

    for i, aa in enumerate(a, 1):
        for bb in a[i:]:
            if aa < bb:
                ans[i - 1] = bb
                break

    return ans


# using stack
def nextLarger(a):
    stack = []
    ans = []

    for x in a[::-1]:
        if stack and x >= stack[-1]:
            stack.pop()
        ans.append(stack.pop() if stack else -1)
        stack.append(x)

    return ans[::-1]


cases = [
        [6, 7, 3, 8],       # [7, 8, 8, -1]
        [4, 2],             # [-1, -1]
        ]
for a in cases:
    print(nextLarger(a))
