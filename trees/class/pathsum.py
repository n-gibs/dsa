class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

root = Node(44)

root.left = Node(17)
root.left.left = Node(8)
root.left.right = Node(32)
root.left.right.left = Node(28)
root.left.right.left.right = Node(29)

root.right = Node(88)
root.right.left = Node(65)
root.right.left.left = Node(54)
root.right.left.right = Node(82)
root.right.left.right.left = Node(76)
root.right.left.right.left.left = Node(68)
root.right.left.right.left.right = Node(80)
root.right.right = Node(97)
root.right.right.left = Node(93)

#root to leaf path sum, return True or False

def pathsum(root, target):

    hasSum = False

    def helper(node, current_sum):
        nonlocal hasSum
        if hasSum: return

        if (node.left is None and node.right is None):
            if node.val is current_sum:
                hasSum = True
            return

        current_sum-= node.val
        if node.left:
            helper(node.left, current_sum)
        if node.right:
            helper(node.right, current_sum)

    helper(root, target)
    return hasSum

print(pathsum(root, 69))