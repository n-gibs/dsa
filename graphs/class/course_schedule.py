#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.Cycle

#is thise a graph problem?
    #pre reqresites, directed graph

# what kind of traversal?
    # directed graphs can have cross edges and back edges
    #cross edges dont find cycles but back edges do

    #dfs helps find back edges, but we need to differentiate between cross and back edges

    #DFS with bookkeeping ( directed graphs have no tree reverse)

def can_be_completed(n, a, b):
    """
    Args:
     n(int32)
     a(list_int32)
     b(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #build the graph
    visited = [-1] * n

    adj_list = [[] for _ in range(n)]

    for i in range(len(a)):
        adj_list[a[i]].append(b[i])


    def dfs(node):
        visited[node] =1
        for course in adj_list[node]:
            if visited[course] == -1:
                if not dfs(course):
                    return False
            elif visited[course] == 1:
                return False

        visited[node] = 2
        return True

    for i in range(len(visited)):
        if visited[i] == -1:
            if not dfs(i):
                return False

    return True