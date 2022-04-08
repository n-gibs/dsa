def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None:
        return None

    stack = []
    curr = root
    while curr:
        stack.append(curr)
        curr = curr.left

    newRoot = stack.pop()
    curr = newRoot

    while stack:
        prev = stack.pop()
        curr.left = prev.right
        curr.right = prev
        curr = prev

    curr.left = None
    curr.right = None
    return newRoot

#recursive
def flip_upside_down(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    if root is None:
        return
    return helper(root)

def helper(node):

    stack=[]

    while node.left:
        stack.append(node)
        node = node.left

    while len(stack)>0:
        prev = stack[-1]
        prev.left.left = prev.right
        prev.left.right = prev
        prev.left = None
        prev.right = None
        stack.pop(-1)

    return node
