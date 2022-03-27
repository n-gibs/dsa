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

def search(root, key):
    curr = root

    while curr:
        if key == curr.val:
            return curr

        if key < curr.val:
            curr = curr.left

        else:
            curr = curr.right

    return None

print(search(root, 32).val)