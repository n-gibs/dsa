#62. Unique Paths
#https://leetcode.com/problems/unique-paths/

#There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

def find_path(n, k):

    if k == 0 or k == n: return 1

    table = [[[] * n] * k]

    for row in range(n):
        table[row][0] = 1

    for col in range(k):
        table[col][col] = 1

    for row in range(2, n):
        for col in range(1, min(row, k)):
            table[row][col] = table[row-1][col] + table[row][col-1]


    return table[n-1][k-1]