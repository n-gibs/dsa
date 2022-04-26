#Path Sum II

#https://leetcode.com/problems/path-sum-ii/

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

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


def pathsum(root, target):

    result = []
    if root is None: return result

    def helper(node, current_sum, partial):

        current_sum -= node.val
        partial.append(node.val)
        print(current_sum)
        if (node.left is None and node.right is None):
            if current_sum == 0:
                result.append(list(partial[:]))
            ##pop when we reach the leaf node
            partial.pop()
            return

        if node.left:
            helper(node.left, current_sum, partial)
        if node.right:
            helper(node.right, current_sum, partial)
        #pop after recursive cases
        partial.pop()


    helper(root, target, [])
    return result

print(pathsum(root, 322))

#69
#150
#251
#423
#425
#322