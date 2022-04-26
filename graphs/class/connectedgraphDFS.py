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