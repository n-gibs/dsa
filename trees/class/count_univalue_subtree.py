class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

# root = Node(44)

# root.left = Node(17)
# root.left.left = Node(8)
# root.left.right = Node(32)
# root.left.right.left = Node(28)
# root.left.right.left.right = Node(29)

# root.right = Node(88)
# root.right.left = Node(65)
# root.right.left.left = Node(54)
# root.right.left.right = Node(82)
# root.right.left.right.left = Node(76)
# root.right.left.right.left.left = Node(68)
# root.right.left.right.left.right = Node(80)
# root.right.right = Node(97)
# root.right.right.left = Node(93)

root = Node(3)

root.left = Node(10)
root.left.left = Node(5)
root.left.right = Node(5)
root.left.right.left = Node(5)
root.left.right.left.right = Node(5)

# root.right = Node(88)
# root.right.left = Node(65)
# root.right.left.left = Node(54)
# root.right.left.right = Node(82)
# root.right.left.right.left = Node(76)
# root.right.left.right.left.left = Node(68)
# root.right.left.right.left.right = Node(80)
# root.right.right = Node(97)
# root.right.right.left = Node(93)

#int function getUnivalueSubtreeCount(TreeNode root) {

#     int univalCount = 0
#     if(root is null) return univalCount

#     boolean function getCountHelper(TreeNode node){

#         if(node.left is null and node.right is null){
#             univalCount++
#             return true
#         }

#         uvalFlag = true

#         if(node.left is not null){
#             uvalFlag = getCountHelper(node.left)
#                         and (node.val == node.left.val)
#         }
#         if(node.right is not null){
#             uvalFlag = getCountHelper(node.right)
#                         and (node.val == node.right.val)
#                         and uvalFlag
#         }
#         if(uvalFlag) univalCount++
#         return uvalFlag
#     }

#     getCountHelper(root)
#     return univalCount
# }


#botttom up
#univalue means subtree are the same values

def count_univalue(root):

    uvCount = [0]

    if root is None:
        return uvCount[0]

    def helper(node: Node):

        if node.left is None and node.right is None:
            uvCount[0]+=1
            return True

        uvalFlag = True

        if node.left:
            uvalFlag = helper(node.left) and node.val == node.left.val

        if node.right:
            uvalFlag = helper(node.right) and node.val == node.right.val and uvalFlag

        #operations happening affer recursive case
        if uvalFlag: uvCount[0] +=1

        return uvalFlag

    helper(root)
    return uvCount[0]

print(count_univalue(root))