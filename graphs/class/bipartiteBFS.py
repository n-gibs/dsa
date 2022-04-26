#785. Is Graph Bipartite?

#https://leetcode.com/problems/is-graph-bipartite/

#There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

#     * There are no self-edges (graph[u] does not contain u).
#     * There are no parallel edges (graph[u] does not contain duplicate values).
#     * If v is in graph[u], then u is in graph[v] (the graph is undirected).
#     * The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.


#is graph problem? yes in questions
# what kind of traversal will help us
    # assign subet as traverse
    # if see visited, check which subset its in
    # DFS to easily hot to next un visited neighbot

#code it up
    #build graph?
        # edge lsit -> adj_list
    #outer loop?
        # yes, disjointed/ un connected graphs can be bipartite

    #throw nodes into a set and get size of set

    #do we need parent array? no, we know if its a parent/child subets are different

def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # Write your code here.

    adj_list = [[] for _ in range(num_of_people)]

    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])
    n = len(adj_list)

    distance = [-1] * n

    def bfs(node):
        q = [node]
        distance[node] = 1
        while q:
            curr = q.pop(0)

            for neighbor in adj_list[curr]:
                if distance[neighbor] == -1:
                    q.append(neighbor)
                    distance[neighbor] = 1 + distance[curr]

                else:
                    if distance[neighbor] == distance[curr]:
                        return False
        return True


    for node in range(n):
        if distance[node] == -1:
            if not bfs(node):
                return False
