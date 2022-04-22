from collections import deque
def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     prerequisites(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    adj_list = [[] for _ in range(n)]
    in_degree = [0] * n
    top_sort = []

    for src, dst in prerequisites:
        adj_list[src].append(dst)
        in_degree[dst] += 1

    q = deque()
    for i in range(n):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        top_sort.append(curr)
        for neighbor in adj_list[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    top_sort.reverse()
    return [-1] if len(top_sort) != n else top_sort
