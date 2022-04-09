def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    if not root:
        return True

    stack = [root]

    while stack:
        node = stack.pop()

        if node.left:
            if find_max(node.left) > node.value:
                return False

            stack.append(node.left)

        if node.right:
            if node.right.value < node.value:
                return False
            stack.append(node.right)

    return True

#find max node in sub tree
def find_max(node):
    if not node:
        return None

    while node.right:
        node = node.right

    return node.value
