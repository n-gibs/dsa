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


def successor(root, p):
    #missing case for no sucessor
    if root is None: return None

    if p.right:
        curr = p.right

        while curr.left:
            curr = curr.left

        return curr

    ancestor = None
    curr = root

    while curr.val is not p.val:
        if p.val < curr.val:
            ancestor = curr
            curr = curr.left

        else:
            curr = curr.right

    return ancestor

print(successor(root, root.right.right).val)
