#70. Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/

#You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def stairs(n):

    if n == 1 or n == 2: return n

    table = [None]*3

    for i in range(3, n):
        table[i%3] = table[(i-1)%3] + table[(i-2)%3]

    return table[n%3]