# https://app.codesignal.com/interview-practice/task/TG4tEMPnAc3PnzRCs


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def rec(t, s):
    if t:
        if not (t.right or t.left): # leaf node
            return s == t.value

        return rec(t.right, s - t.value) or rec(t.left, s - t.value)
    else:
        return False


def hasPathWithGivenSum(t, s):
    return rec(t, s)


cases = [
        [{
            "value": 4,
            "left": {
                "value": 1,
                "left": {
                    "value": -2,
                    "left": None,
                    "right": {
                        "value": 3,
                        "left": None,
                        "right": None
                        }
                    },
                "right": None
                },
            "right": {
                "value": 3,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 2,
                    "left": {
                        "value": -2,
                        "left": None,
                        "right": None
                        },
                    "right": {
                        "value": -3,
                        "left": None,
                        "right": None
                        }
                    }
                }
            }, 7],      # True
        [{
            "value": 4,
            "left": {
                "value": 1,
                "left": {
                    "value": -2,
                    "left": None,
                    "right": {
                        "value": 3,
                        "left": None,
                        "right": None
                        }
                    },
                "right": None
                },
            "right": {
                "value": 3,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 2,
                    "left": {
                        "value": -4,
                        "left": None,
                        "right": None
                        },
                    "right": {
                        "value": -3,
                        "left": None,
                        "right": None
                        }
                    }
                }
            }, 7],      # False
        ]

def make_tree(t: dict):
    if t:
        node = Tree(t["value"])
        node.left = make_tree(t["left"])
        node.right = make_tree(t["right"])

        return node
    else:
        return None

def print_tree(t):
    if t:
        print(t.value)

        print_tree(t.left)
        print_tree(t.right)

for tree, s in cases:
    t = make_tree(tree)
    print(hasPathWithGivenSum(t, s))
