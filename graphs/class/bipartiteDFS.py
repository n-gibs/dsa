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

    visited = [-1] * n
    color = [-1] * n
    is_bipartite = True

    def dfs(node):
        nonlocal is_bipartite
        if not is_bipartite: return


        visited[node] = 1

        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                color[neighbor] = 1-color[node]
                dfs(neighbor)

            else:
                if color[neighbor] == color[node]:
                    is_bipartite  = False


    for node in range(num_of_people):
        if visited[node] == -1:
            dfs(node)


    return is_bipartite