def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    if root is None: return result

    def helper(node, partial):
        partial.append(node.value)

        if node.left is None and node.right is None:
            result.append(partial[:])
            partial.pop()
            return

        if node.left:
            helper(node.left, partial)

        if node.right:
            helper(node.right, partial)

        partial.pop()

    helper(root, [])
    return result