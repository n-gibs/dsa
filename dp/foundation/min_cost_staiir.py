#746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

#You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.
import math

def min_cost_stair(cost):

    n = len(cost)
    table = [0]*n
    table[0] = cost[0]
    table[1] = cost[1]

    for i in range(2, n):
        table[i] = cost[i] + min(table[i - 1], table[i - 2])

    return min(table[n - 1], table[n - 2])


# stairs = [10,15,20]

print(min_cost_stair([10,15,20]))

def min_cost_class_sol(cost):

    n = len(cost)
    cost.append(0)

    table = [0]*(n+1)
    table[0] = cost[0]
    table[1] = cost[1]

    for i in range(2, n+1):
        table[i] = cost[i] + min(table[i - 1], table[i - 2])

    return table[-1]