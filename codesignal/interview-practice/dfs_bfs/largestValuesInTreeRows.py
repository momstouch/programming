# https://app.codesignal.com/interview-practice/task/m9vC4ALaAeudkwRTF

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def largestValuesInTreeRows(t):
    if not t:
        return []

    q1 = [t]
    ans = []

    while q1:

        q2 = []

        max_val = -1001
        while q1:
            q = q1.pop(0)
            max_val = max(q.value, max_val)
            if q.left:
                q2.append(q.left)
            if q.right:
                q2.append(q.right)

        ans.append(max_val)

        if q2:
            max_val = -1001
            while q2:
                q = q2.pop(0)
                max_val = max(q.value, max_val)
                if q.left:
                    q1.append(q.left)
                if q.right:
                    q1.append(q.right)

            ans.append(max_val)

    return ans


cases = [
        {
            "value": -1,
            "left": {
                "value": 5,
                "left": None,
                "right": None
                },
            "right": {
                "value": 7,
                "left": None,
                "right": {
                    "value": 1,
                    "left": None,
                    "right": None
                    }
                }
            },      # [-1, 7, 1]
        {
            "value": -1,
            "left": {
                "value": 5,
                "left": None,
                "right": None
                },
            "right": {
                "value": 7,
                "left": None,
                "right": {
                    "value": 1,
                    "left": {
                        "value": 5,
                        "left": None,
                        "right": None
                        },
                    "right": None
                    }
                }
            },      # [-1, 7, 1, 5]
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

    print(largestValuesInTreeRows(t))
