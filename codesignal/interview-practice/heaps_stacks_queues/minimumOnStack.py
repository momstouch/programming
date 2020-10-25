# https://app.codesignal.com/interview-practice/task/gnZYGn367s4yaHvRr/description

def operation_parser(operation):
    try:
        cmd, num = operation.split(' ')
        num = int(num)
    except ValueError:
        cmd = operation
        num = None

    return cmd, num

def minimumOnStack_fromhint(operations):
    stack = []
    minelem = None

    ans = []

    for op in operations:
        cmd, num = operation_parser(op)

        if cmd == "push":
            if not stack:
                stack.append(num)
                minelem = num
            else:
                if minelem > num:
                    stack.append(2 * num - minelem)
                    minelem = num
                else:
                    stack.append(num)
        elif cmd == "pop":
            if stack:
                num = stack.pop()
                if num < minelem:
                    num = minelem = 2 * minelem - num
                #print("pop:", num, ", min:", minelem)
        elif cmd == "min":
            if stack:
                ans.append(minelem)

        #print(op, stack, minelem)

    return ans


# additional O(n) memory space
def minimumOnStack(operations):
    stack = []
    minval = None

    ans = []

    for op in operations:
        cmd, num = operation_parser(op)

        if cmd == "push":
            if not stack:
                stack.append((num, None))
                minval = num
            else:
                stack.append((num, minval))
                minval = num if num < minval else minval
        elif cmd == "pop":
            if stack:
                v, minval = stack.pop()
        elif cmd == "min":
            if stack:
                ans.append(minval)

    return ans


cases = [
        ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"],
        # [10, 5, 5, 5, 10]
        ]
for operations in cases:
    print(minimumOnStack(operations))
