#is bipartite
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

def is_bipartite(edges):

    #get n
    #sets ignore duplicates
    s = set()
    for src, dst in edges:
        s.add(src)
        s.add(dst)
    n = s.size()

    #create adj_list from n
    adj_list = [[] for _ in range(n)]

    for src, dst in edges:
        adj_list[src] = dst
        adj_list[dst] = src

    subsets = [-1] * n
    # [-1, -1, -1, -1]

    for node in range(n):
        if subsets[node] == -1:
            if not dfs(node):
                return False

    def dfs(node):

        for neighbor in adj_list[node]:
            if subsets[neighbor] == -1:
                # assign opposite subset
                #if edge exists, neighbor needs to be the opposite subset
                # 1 - (-1) = 1
                subsets[neighbor] = 1 - subsets[node]
                dfs(neighbor)
            else: #seen something seen before
                if subsets[node] == subsets[neighbor]:
                    return False
                return True

    return True