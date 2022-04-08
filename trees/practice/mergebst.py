"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def merge_two_binary_search_trees(root1, root2):
    """
    Args:
     root1(BinaryTreeNode_int32)
     root2(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """

    merged = []

    def dfs(node):
        if node is None:
            return

        if node.left is None and node.right is None:
            merged.append(node)
            return

        if node.left is not None:
            dfs(node.left)

        merged.append(node)

        if node.right is not None:
            dfs(node.right)


    dfs(root1)
    dfs(root2)
    merged.sort(key=lambda x:x.value)

    def helper(start, end):

        if start > end:
            return None

        else :
            mid = start + (end-start) // 2
            merged[mid].left = helper(start, mid-1)
            merged[mid].right = helper(mid+1, end)

        return merged[mid]


    return helper(0, len(merged)-1)
