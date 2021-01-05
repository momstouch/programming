import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if not root:
        return False
    
    if root.value == value:
        return True
    
    if root.value < value:
        return contains(root.right, value)
    else:
        return contains(root.left, value)
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
assert contains(n2, 3) == True
