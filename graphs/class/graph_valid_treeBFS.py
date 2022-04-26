#Graph Valid Tree
#https://leetcode.com/problems/graph-valid-tree/

# An undirected graph is tree if it has following properties.
# 1) There is no cycle.
# 2) The graph is connected.
# For an undirected graph we can either use BFS or DFS to detect above two properties.
#--------------


#1 can it be modeled as graph problem?
    #yes graph valid tree
#2 what traversal will help us?
    #connect component = 1
    #no cycle
#3 extension, cycle detection
#4 code it up -> do we need to build graph
    #do we need to build the graph(better data structure
        #edge list -> adj list
    # mutiple traversals?
        # yes visit every node, make aure only 1 connect component
    #code up (DFS)
        #then add cycle detection
#BFS
def valid_tree(n, edges):
    #build graph
    #list of lists
    '''
    [
        0 | []
        1 | []
        3 | []
        4 | []
    ]
    '''
    adj_list = [[] for _ in range(n)]
    # adj_list = dict(list())
    #undirected
    #O(m)
    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visited = [-1] * n
    parents = [-1] * n
        #parent[a] = b
    def bfs(node):
        queue = [node]
        visited[node] = 1

        while queue:
            curr = queue.pop(0)

            for neighbor in adj_list[curr]:

                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parents[node]= curr
                    queue.append(neighbor)

                else:
                     # seeing something ive seen before
                    if parents[curr] != neighbor: #if neigbor is parent
                        return False
                return True

    components = 0
    for i in range(n):
        if visited[i] == -1: #unvisited
            #traverse
            if components == 1: return False
            if not bfs(i):
                return False #if there was cycle #updates visited list
            components += 1

    return True
