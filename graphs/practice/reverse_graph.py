class Node:
    def __init__(self):
        self.val = 0
        self.neighbors = []

def build_graph(node):

    visited = set()

    def dfs(node):
        new_node = Node()
        new_node.val = node.val
        visited.add(new_node.val)
        # map[node] = Node(node.val)

        for child in node.children:
            if child not in visited:
                new_neighbor = dfs(child)
            else:
                new_neighbor = visited[child]

            new_neighbor.neighbors.append(new_node)
        return new_node

    return dfs(node)

def build_graph_bfs(node):
    visited = set()
    q = [node]

    new_node = Node()
    new_node.val = node.val

    while q:
        curr = q.pop(0)

        for child in curr.neighbors:
            if child not in visited:
                new_child = Node()
                new_child.val = child.val
                q.append(child)
                visited[child] = new_child

            else:
                new_child = visited[child]

            new_child.neighbors.append(visited[node])

    return new_node
