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


def sortedListToBST(self, head):
    if not head:
        return
    if not head.next:
        return BinaryTreeNode(head.val)
    # here we get the middle point,
    # even case, like '1234', slow points to '2',
    # '3' is root, '12' belongs to left, '4' is right
    # odd case, like '12345', slow points to '2', '12'
    # belongs to left, '3' is root, '45' belongs to right
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # tmp points to root
    tmp = slow.next
    # cut down the left child
    slow.next = None
    root = BinaryTreeNode(tmp.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root