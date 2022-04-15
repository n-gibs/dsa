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
