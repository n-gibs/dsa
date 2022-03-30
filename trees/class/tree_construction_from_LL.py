class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    input = []
    while head:
        input.append(head.value)
        head = head.next


    return bsthelper(input,0,len(input)-1)

def bsthelper(input,start,end):
    if start > end:
        return
    if start == end:
        return BinaryTreeNode(input[start])

    mid = start + (end-start)//2

    rootNode = BinaryTreeNode(input[mid])
    rootNode.left = bsthelper(input,start,mid-1)
    rootNode.right = bsthelper(input,mid+1,end)

    return rootNode


def sorted_list_to_bst(head):
    """
    Args:
     head(LinkedListNode_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.

    list_size = 0
    node = head

    while node != None:
        list_size += 1
        node = node.next


    root = helper(head, list_size)

    return root


def helper(head, list_size):
    # Base Case
    if head == None or list_size == 0:
        return None

    # Recursive Case
    mid = list_size // 2
    node = head

    for _ in range(mid-1):
        node = node.next

    root_node = node.next if node.next else node
    head_right = root_node.next
    node.next = None

    root = BinaryTreeNode(root_node.value)

    root_left = helper(head, mid)
    root_right = helper(head_right, list_size - mid - 1)

    root.left = root_left
    root.right = root_right

    return root