# https://app.codesignal.com/interview-practice/task/tXN6wQsTknDT6bNrf

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def get_left_seq(t, out: list):
    if t:
        out.append(t.value)
        get_left_seq(t.left, out)
        get_left_seq(t.right, out)
    else:
        out.append(1001)


def is_same(t, left):
    if t:
        return left.pop(0) == t.value and \
                is_same(t.right, left) and \
                is_same(t.left, left)
    else:
        return left.pop(0) == 1001


def isTreeSymmetric_mine(t):
    if not t:
        return True

    left = []
    get_left_seq(t.left, left)

    return is_same(t.right, left)


def isTreeSymmetric(t):
    def isSymm(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False

        return l.value == r.value and \
                isSymm(l.left, r.right) and \
                isSymm(l.right, r.left)

    if not t:
        return True
    return isSymm(t.left, t.right)


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
        {
            "value": 1,
            "left": {
                "value": 2,
                "left": {
                    "value": 3,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 4,
                    "left": None,
                    "right": None
                    }
                },
            "right": {
                "value": 2,
                "left": {
                    "value": 4,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 3,
                    "left": None,
                    "right": None
                    }
                }
            },      # True
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
                "value": 2,
                "left": None,
                "right": {
                    "value": 3,
                    "left": None,
                    "right": None
                    }
                }
            },      # Fase
        {
                "value": 99,
                "left": {
                    "value": 100,
                    "left": None,
                    "right": None
                    },
                "right": {
                    "value": 99,
                    "left": None,
                    "right": None
                    }
                },      # False
        ]

for tree in cases:
    t = make_tree(tree)
    print(isTreeSymmetric(t))
