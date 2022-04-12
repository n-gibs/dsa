def connected_components(n, edges):
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

        #recursive set approach
    def dfs(node):
        visited[node] = 1

        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                dfs(neighbor)

    components = 0
    for i in range(n):
        if visited[i] == -1: #unvisited
            #traverse
            dfs(i) #updates visited list
            components += 1

    return components