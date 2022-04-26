#210. Course Schedule II
#https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

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
