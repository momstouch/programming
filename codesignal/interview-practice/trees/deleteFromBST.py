# https://app.codesignal.com/interview-practice/task/oZXs4td52fsdWC9kR


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def deleteFromBST_bad_readability(t, queries):
    for q in queries:
        tt = t
        pre = None

        while tt:
            if tt.value > q:
                pre = tt
                tt = tt.left
            elif tt.value < q:
                pre = tt
                tt = tt.right
            else: # found
                if tt.left:
                    tmp_pre = None
                    tmp = tt.left
                    while tmp.right:
                        tmp_pre = tmp
                        tmp = tmp.right

                    if tmp_pre:
                        tmp_pre.right = tmp.left
                    else:
                        tt.left = tmp.left

                    tt.value = tmp.value

                elif tt.right:
                    if pre:
                        if pre.value < q:
                            pre.right = tt.right
                        else:
                            pre.left = tt.right
                    else:
                        t = tt.right
                else: # leaf
                    if pre:
                        if pre.value < q:
                            pre.right = None
                        else:
                            pre.left = None
                    else:
                        t = None

                break

    return t


def deleteFromBST(t, queries):
    def remove_rightmost(t):
        if t.right is None:
            return t.left
        else:
            t.right = remove_rightmost(t.right)
        return t

    def get_rightmost(t):
        if t is None:
            return None
        while t.right:
            t = t.right
        return t.value

    def find(t, q):
        if t is None:
            return None

        if t.value == q:
            if t.left:
                t.value = get_rightmost(t.left)
                t.left = remove_rightmost(t.left)
            else:
                t = t.right
        elif t.value < q:
            t.right = find(t.right, q)
        else:
            t.left = find(t.left, q)
        return t

    for q in queries:
        t = find(t, q)

    return t


def make_tree(t: dict):
    if t:
        node = Tree(t["value"])
        node.left = make_tree(t["left"])
        node.right = make_tree(t["right"])

        return node
    else:
        return None


cases = [
        (
            {
                "value": 5,
                "left": {
                    "value": 2,
                    "left": {
                        "value": 1,
                        "left": None,
                        "right": None
                        },
                    "right": {
                        "value": 3,
                        "left": None,
                        "right": None
                        }
                    },
                "right": {
                    "value": 6,
                    "left": None,
                    "right": {
                        "value": 8,
                        "left": {
                            "value": 7,
                            "left": None,
                            "right": None
                            },
                        "right": None
                        }
                    }
                },
            [4, 5, 6]
            ),
        (
            {
                "value": 3,
                "left": {
                    "value": 2,
                    "left": None,
                    "right": None
                    },
                "right": None
                },
            [1, 2, 3, 5]
            ),
        (
            {
                "value": 3,
                "left": {
                    "value": 2,
                    "left": {
                        "value": 1,
                        "left": None,
                        "right": None
                        },
                    "right": None
                    },
                "right": {
                    "value": 5,
                    "left": None,
                    "right": None
                    }
                },
            [3, 2, 1]
            ),
        ]
for dic_tree, queries in cases[-1:]:
    t = make_tree(dic_tree)
    print(deleteFromBST(t, queries))
