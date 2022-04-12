#1 can it be modeled as graph problem?
#   do we have an easy way to get neighbors?
#2 what traversal will help us
#3 extension, count traversal it takes to explore whole graph
#4 code it up -> do we need to build graph
    #do we need to build the graph(better data structure
        #edge list -> adj list
    # mutiple traversals?
        # we have more than one component
    #code up base BFS/DFS
        #then add extension

#n is number of nodes labeled 0 to n-1
#list of edges [[0,1], [1,3], [3.4]]
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
    #undirected
    #O(m)
    for src, dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    visited = [-1] * n

    def bfs(node):

        queue = [node]
        visited[node] = 1

        while queue:
            curr = queue.pop(0)
            for neighbor in adj_list[curr]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    queue.append(neighbor)

    components = 0
    for i in range(n):
        if visited[i] == -1: #unvisited
            #traverse
            bfs(i) #updates visited list
            components += 1

    return components
