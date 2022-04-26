#323. Number of Connected Components in an Undirected Graph
#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

#Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

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
