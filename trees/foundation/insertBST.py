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
root.right.right = Node(97)
root.right.left = Node(65)

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

def insert(root, val):
    new = Node(val)

    prev = None
    curr = root

    while curr is not None:
        if val == curr.val:
            return

        if val < curr.val:
            prev = curr
            curr = curr.left

        else:
            prev = curr
            curr = curr.right

    if val < prev.val:
        prev.left = new
    else:
        prev.right = new

    return root

newroot = insert(root, 33)
# print(insert(root, 33))
print(search(newroot, 33))