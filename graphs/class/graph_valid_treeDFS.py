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
    components = 0
    for i in range(n):
        if visited[i] == -1: #unvisited
            #traverse
            if components > 0: return False
            if dfs(i):
                return False #if there was cycle #updates visited list
            components += 1


    #recursive set approach
    def dfs(node):
        visited[node] = 1
        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                parents[neighbor] = node
                if not dfs(neighbor): return False
            else: # seeing something ive seen before
                if parents[node] != neighbor: #back edge
                    return False
            return True

    return True