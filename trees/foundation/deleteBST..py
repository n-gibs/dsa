class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

root = Node(44)

root.left = Node(17)
root.right = Node(88)
root.left.left = Node(8)
root.left.right = Node(32)
root.left.right.left = Node(28)
root.left.right.left.right = Node(29)
root.right.right = Node(97)
root.right.right.left = Node(93)
root.right.left = Node(65)
root.right.left.left = Node(54)
root.right.left.right = Node(82)
root.right.left.right.left = Node(76)
root.right.left.right.left.left = Node(68)
root.right.left.right.left.right = Node(80)

def search(root, val):
    curr = root

    while curr:
        if val == curr.val:
            return curr

        if val < curr.val:
            curr = curr.left

        else:
            curr = curr.right

    return None

def delete(root, val):

    #search for node
    prev = None
    curr = root

    while curr:
        if val == curr.val:
            break

        elif val < curr.val:
            prev = curr
            curr = curr.left

        else:
            prev = curr
            curr = curr.right

    if curr is None:
        return root

    #case 1 leaf node to be deleted

    if curr.left is None and curr.right is None:
        if curr == prev.left:
            prev.left = None
        else:
            prev.right = None

    #case 2 - curr has 1 child
    child = None

    #test for case 2 and get child pointer
    if curr.left is None and curr.right:
        child = curr.right

    elif curr.left and curr.right is None:
        child = curr.right

    #if case 2 is true, set
    if child:
        #if current was the left child of parent
        if curr == prev.left:
            prev.left = child
        else: #if curent was right child of parents
            prev.right = child

        return root

    #case 3 node to delte has 2 children

    if curr.left and curr.right:
        #prev to successor
        prev = None
        #sucecssor, leaf node
        succ = curr.right

        #find sucessor and prev to successor
        while succ.left:
            prev = succ
            succ = succ.left

        #copy successor value to current value
        curr.val = succ.val

        #if successor is the left child of prev
        if succ.val == prev.left:
            prev.left = succ.right

        else: # if successor is the right child of prev
            prev.right = succ.right

        return root
