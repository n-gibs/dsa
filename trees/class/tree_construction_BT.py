class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

preorder = [3,9,20,15,7]
#3 is the root

inorder = [9.3,15,20,7]

def tree_construction(inorder, preorder):

    inorder_dict = { i : inorder[i] for i in range(0, len(inorder) ) }
    def helper(preorder, pstart, pend, inorder, istart, iend):
        root = preorder[pstart]

        root_idx = inorder.index(root) #use hashmap here

        count = root_idx - istart
        root = Node(preorder[root_idx])

        root.left = helper(preorder, pstart+1, pstart+count, inorder, istart, root_idx -1)

        root.right = helper(preorder, pstart+count+1, pend, inorder, root_idx+1, iend)

        return root

    helper(preorder, 0, len(preorder) -1, inorder, 0, len(inorder) -1)

root = tree_construction(inorder, preorder)
