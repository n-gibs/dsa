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

def bfs(root):

    if root is None:
        return root

    #make queue
    queue = []
     #add root to queue
    queue.append(root)

    result = []

    while queue:
        node = queue.pop()

        if node.right:
            queue.append(node.right)

        if node.left:
            queue.append(node.left)

        result.append(node.val)

    return result


print(bfs(root))