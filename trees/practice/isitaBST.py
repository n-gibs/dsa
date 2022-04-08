# def is_bst(root):
#     """
#     Args:
#      root(BinaryTreeNode_int32)
#     Returns:
#      bool
#     """
#     # Write your code here.
#     if root is None:
#         return True
#     stack = []
#     prev = None
#     while True:
#         while root:
#             stack.append(root)
#             root = root.left
#         if len(stack) == 0:
#             break
#         root = stack.pop()
#         if prev and prev.value > root.value:
#             return False
#         prev = root
#         root = root.right
#     return True

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

def find_max(node):
    if not node:
        return None

    while node.right:
        node = node.right

    return node.value
