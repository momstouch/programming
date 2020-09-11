# https://app.codesignal.com/interview-practice/task/PhNPP45hZGNwpPchi

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

# Try to solve this task without using recursion
def traverseTree(t):
    queue = [t]
    answer = []

    while queue:
        q = queue.pop(0)
        if q:
            answer.append(q.value)
            queue.append(q.left)
            queue.append(q.right)

    return answer


cases = [
        {
            "value": 1,
            "left": {
                "value": 2,
                "left": None,
                "right": {
                    "value": 3,
                    "left": None,
                    "right": None
                    }
                },
            "right": {
                "value": 4,
                "left": {
                    "value": 5,
                    "left": None,
                    "right": None
                    },
                "right": None
                }
            },  # [1, 2, 4, 3, 5]
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

    print(traverseTree(t))
