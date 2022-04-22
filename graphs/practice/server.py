def find_critical_connections(number_of_servers, connections):
    """
    Args:
     number_of_servers(int32)
     connections(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.

    adj_list = [[] for _ in range(number_of_servers)]

    for src, dst in connections:
        adj_list[src].append(dst)
        adj_list[dst].append(src)


    visited = [-1]*number_of_servers

    parent = [-1]*number_of_servers
    arrival = [-1]*number_of_servers
    oldest_arrival = [-1]*number_of_servers

    timestamp = 0

    results = []

    def dfs(src):
        nonlocal timestamp
        arrival[src] = timestamp
        oldest_arrival[src] = arrival[src]
        timestamp += 1
        visited[src] = 1

        for neighbor in adj_list[src]:
            if visited[neighbor] == -1: # Tree edge
                parent[neighbor] = src
                # DFS
                neighbor_arrival = dfs(neighbor)
                oldest_arrival[src] = min(oldest_arrival[src], neighbor_arrival)

            else:
                if neighbor != parent[src]:
                    oldest_arrival[src] = min(oldest_arrival[src], arrival[neighbor]) # backedge

        if oldest_arrival[src] == arrival[src] and src !=0: # Critical component found b/c "leaf node"
            results.append((src,parent[src]))

        timestamp+=1
        return oldest_arrival[src]


    dfs(0)

    if not results: return [[-1, -1]]

    return results
