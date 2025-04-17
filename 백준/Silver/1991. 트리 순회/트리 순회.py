tree = {}
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

def preOrder(root):
    if root == ".":
        return ''
    print(tree[root].val, end = '')
    preOrder(tree[root].left)
    preOrder(tree[root].right)
    return ''

def inOrder(root):
    if root == ".":
        return ''
    inOrder(tree[root].left)
    print(tree[root].val, end = '')
    inOrder(tree[root].right)
    return ''

def postOrder(root):
    if root == ".":
        return ''
    postOrder(tree[root].left)
    postOrder(tree[root].right)
    print(tree[root].val, end = '')
    return ''

n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())

for item, left, right in inputs:
    tree[item] = TreeNode(item, left, right)
    
print(preOrder('A'))
print(inOrder('A'))
print(postOrder('A'))