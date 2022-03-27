from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

root = Node(44)

root.left = Node(17)
root.left.left = Node(8)
root.left.right = Node(32)
root.left.right.left = Node(28)
root.left.right.left.right = Node(29)

root.right = Node(88)
root.right.left = Node(65)
root.right.left.left = Node(54)
root.right.left.right = Node(82)
root.right.left.right.left = Node(76)
root.right.left.right.left.left = Node(68)
root.right.left.right.left.right = Node(80)
root.right.right = Node(97)
root.right.right.left = Node(93)

#returns array of the right most nodes

def right_side(root):

    result = []

    if root is None: result

    #make queue
    queue = deque()

    #add root to queue
    queue.append(root)

    while queue:
        count = len(queue)
        temp = []

        # needed for 2D array
        for _ in range(count):

            node = queue.popleft()

            temp = node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(temp)


    return result


print(right_side(root))