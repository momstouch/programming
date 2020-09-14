# https://app.codesignal.com/interview-practice/task/2oxNWXTS8eWBzvnRB

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def dfs(t, num, sums):
    num.append(str(t.value))

    if not t.left and not t.right:
        sums[0] += int("".join(num))
    if t.left:
        dfs(t.left, num, sums)
    if t.right:
        dfs(t.right, num, sums)
    num.pop()

def digitTreeSum(t):
    if not t:
        return 0

    nums = []
    sums = [0]

    dfs(t, nums, sums)

    return sums[0]


def digitTreeSum2(t, acc = 0):
    if not t:
        return 0

    if not t.left and not t.right:
        return acc * 10 + t.value

    return digitTreeSum2(t.left, acc * 10 + t.value) + \
            digitTreeSum2(t.right, acc * 10 + t.value)


cases = [
        {
            "value": 1,
            "left": {
                "value": 0,
                "left": {
                    "value": 3,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 1,
                    "left": None,
                    "right": None
                    }
                },
            "right": {
                "value": 4,
                "left": None,
                "right": None
                }
            },      # 218
        ]

def make_tree(tree):
    if not tree:
        return None

    t = Tree(tree["value"])
    if tree["left"]:
        t.left = make_tree(tree["left"])
    if tree["right"]:
        t.right = make_tree(tree["right"])

    return t

for case in cases:
    t = make_tree(case)

    print(digitTreeSum(t))
