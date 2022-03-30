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

#botttom up
#Given the root of a binary tree, return the length of the diameter of the tree.
#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#The length of a path between two nodes is represented by the number of edges between them.

# def diameter(root):

#     maxDiameter = [0]

#     if root is None:
#         return maxDiameter[0]

#     def helper(node):

#         if node.left is None and node.right is None:
#             return 0

#         lmax, rmax = 0, 0

#         if node.left:
#             lmax = helper(node.left) +1

#         if node.right:
#             rmax = helper(node.right) +1

#         #operations happening affer recursive case
#         currentmax = maxDiameter[0]
#         maxDiameter[0] = max(lmax + rmax, currentmax)

#         return max(lmax, rmax)

#     helper(root)
#     return maxDiameter[0]

# print(diameter(root))

def diameter(root):

    maxDiameter = 0

    if root is None:
        return maxDiameter

    def helper(node):
        nonlocal maxDiameter
        if node.left is None and node.right is None:
            return 0

        lmax, rmax = 0, 0

        if node.left:
            lmax = helper(node.left) +1

        if node.right:
            rmax = helper(node.right) +1

        #operations happening affer recursive case
        currentmax = maxDiameter
        maxDiameter = max(lmax + rmax, currentmax)

        return max(lmax, rmax)

    helper(root)
    return maxDiameter

print(diameter(root))
