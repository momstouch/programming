# https://app.codesignal.com/interview-practice/task/jAKLMWLu8ynBhYsv6

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def kthSmallestInBST_mine(t, k):
    def search(t, k, out):
        if t:
            search(t.left, k, out)
            if len(out) == k:
                return
            out.append(t.value)
            search(t.right, k, out)

    out = []
    search(t, k, out)
    return out[-1]

#super pythonic code below
def kthSmallestInBST(t, k):
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node.value
            yield from dfs(node.right)

    bst_iter = dfs(t)
    for _ in range(k):
        ans = next(bst_iter)

    return ans


def make_tree(t: dict):
    if t:
        node = Tree(t["value"])
        node.left = make_tree(t["left"])
        node.right = make_tree(t["right"])

        return node
    else:
        return None


cases = [
        [
            {
                "value": 3,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 5,
                    "left": {
                        "value": 4,
                        "left": None,
                        "right": None
                        },
                    "right": {
                        "value": 6,
                        "left": None,
                        "right": None
                        }
                    }
                },
            4
            ],      # 5
        [
            {
                "value": 1,
                "left": {
                    "value": -1,
                    "left": {
                        "value": -2,
                        "left": None,
                        "right": None
                        },
                    "right": {
                        "value": 0,
                        "left": None,
                        "right": None
                        }
                    },
                "right": None
                },
            1
            ],      # -2
        ]

for tree, k in cases:
    t = make_tree(tree)
    print(kthSmallestInBST(t, k))
