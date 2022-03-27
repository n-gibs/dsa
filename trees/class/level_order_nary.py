from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

root = Node(44)
root.children = [Node(32), Node(40), Node(30)]

def bfs(root):

    result = []

    if root is None: result

    #make queue
    queue = deque

    #add root to queue
    queue.append(root)

    while queue:
        count = len(queue)
        temp = []

        # needed for 2D array
        for _ in range(count):

            node = queue.popleft()

            temp.append(node.val)

            for child in node.children:
                queue.append(child)

        result.append(temp)

    return result


print(bfs(root))