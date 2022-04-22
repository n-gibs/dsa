
def zombie_cluster(zombies):
    """
    Args:
     zombies(list_str)
    Returns:
     int32
    """
    # Write your code here.
    visited=[-1]*len(zombies)
    count =0
    q = []

    for v in range(len(zombies)):
        if visited[v]==-1:
            visited[v]=1
            count +=1
            q.append(v)

        while q:
            node = q.pop(0)
            for neighbor in range(len(zombies)):
                if visited[neighbor]==-1 and zombies[node][neighbor]=='1':
                    visited[neighbor]=1
                    q.append(neighbor)


    return count