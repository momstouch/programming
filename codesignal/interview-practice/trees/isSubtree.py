# https://app.codesignal.com/interview-practice/task/mDpAJnDQkJqaYYsCg

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# return true, if t2 is a subtree of t1
def isSubtree(t1, t2):
    def traverse(t):
        if t:
            return str(t.value) + traverse(t.left) + traverse(t.right)
        else:
            return "N"

    trt1 = traverse(t1)
    trt2 = traverse(t2)

    return trt2 in trt1


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

cases = [
        [
            {
                "value": 5,
                "left": {
                    "value": 10,
                    "left": {
                        "value": 4,
                        "left": {
                            "value": 1,
                            "left": None,
                            "right": None
                            },
                        "right": {
                            "value": 2,
                            "left": None,
                            "right": None
                            }
                        },
                    "right": {
                        "value": 6,
                        "left": None,
                        "right": {
                            "value": -1,
                            "left": None,
                            "right": None
                            }
                        }
                    },
                "right": {
                    "value": 7,
                    "left": None,
                    "right": None
                    }
                },
            {
                "value": 10,
                "left": {
                    "value": 4,
                    "left": {
                        "value": 1,
                        "left": None,
                        "right": None
                        },
                    "right": {
                        "value": 2,
                        "left": None,
                        "right": None
                        }
                    },
                "right": {
                    "value": 6,
                    "left": None,
                    "right": {
                        "value": -1,
                        "left": None,
                        "right": None
                        }
                    }
                }
            ],      # True
            ]

for tree1, tree2 in cases:
    t1 = make_tree(tree1)
    t2 = make_tree(tree2)
    print(isSubtree(t1, t2))

