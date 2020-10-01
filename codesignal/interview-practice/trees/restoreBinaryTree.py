# https://app.codesignal.com/interview-practice/task/AaWaYxi8gjtbqgp2M


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def restoreBinaryTree(inorder, preorder):
    if not inorder:
        return None

    t = Tree(preorder[0])
    idx = inorder.index(preorder[0])
    t.left = restoreBinaryTree(inorder[:idx], preorder[1: idx + 1])
    t.right = restoreBinaryTree(inorder[idx + 1: ], preorder[idx + 1: ])

    return t


cases = [
        [
            [4, 2, 1, 5, 3, 6],
            [1, 2, 4, 3, 5, 6]
            ],
        [
            [2, 5],
            [5, 2]
            ],
        ]
for inorder, preorder in cases:
    t = restoreBinaryTree(inorder, preorder)
