class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
# TreeNode function arrayToBst(int[] input) {
#     TreeNode function makeTree(int[] input, int s, int e){
#         if(s > e) return null

#         int mid = s + (e-s)/2

#         TreeNode root = new TreeNode(input[mid])

#         root.left = makeTree(input, s, mid - 1)
#         root.right = makeTree(input, mid + 1, e)

#         return root

#     }
#     return makeTree(input, 0, input.length - 1)
# }

arr = [-10,-3,0,5,9]

def arr_to_BST(nums):

    def helper(nums, start, end):

        if start > end:
            return None


        middle = start + (end-start)//2

        root = Node(nums[middle])

        root.left = helper(nums, start, middle-1)
        root.right = helper(nums, middle +1, end)

        return root

    return helper(nums, 0, len(nums) -1)

root = arr_to_BST(arr)

def inorder(node):
    if node:
        print(node.val)
        inorder(node.left)
        inorder(node.right)

print(inorder(root))