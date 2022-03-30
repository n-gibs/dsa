class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_search_tree(preorder):
    """
    Args:
     preorder(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    if len(preorder) == 0:
        return None

    root = BinaryTreeNode(preorder[0])

    stack = [root]

    #loop through array from index 1
    for value in preorder[1:]:
        node = BinaryTreeNode(value)

        #value is less than the last stack value
        if node.value < stack[-1].value:
            #last stack node.left points to new node
            stack[-1].left = node
        else:
            # while theres a stack and the last value is less than the new node
            while stack and stack[-1].value < node.value:
                #remove the last node
                last_node = stack.pop()
            #point last_node.right to new node
            last_node.right = node

        #append the new node to the stack
        stack.append(node)

    return root