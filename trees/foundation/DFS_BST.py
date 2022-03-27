class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

root = Node(44)

root.left = Node(17)
root.right = Node(88)
root.left.left = Node(8)
root.left.right = Node(32)
root.left.right.left = Node(28)
root.left.right.left.right = Node(29)
root.right.right = Node(97)
root.right.right.left = Node(93)
root.right.left = Node(65)
root.right.left.left = Node(54)
root.right.left.right = Node(82)
root.right.left.right.left = Node(76)
root.right.left.right.left.left = Node(68)
root.right.left.right.left.right = Node(80)

def preorder(node):
    if node:
        #from left
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)