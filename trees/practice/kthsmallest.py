#iterative
def get_k_smallest(root, k):

    if root is None: return None #throw error

    stack = [root]
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        #inorder traversal
        k-=1
        if k == 0:
            return curr.val

        curr = curr.right

#brute force
def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    if root is None: return None
    arr = []
    def inorder(root):
        arr.append(root.val)
        if root.left:
            inorder(root.left)

        if len(arr) == k-1: return arr[-1]

        if root.right:
            inorder(root.right)

    inorder(root)
