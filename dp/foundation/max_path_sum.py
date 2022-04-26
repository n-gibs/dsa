#https://www.geeksforgeeks.org/maximum-path-sum-matrix/

# Given a matrix of N * M. Find the maximum path sum in matrix. The maximum path is sum of all elements from first row to last row where you are allowed to move only down or diagonally to left or right. You can start from any element in first row.

def max_sum(grid):
    m = len(grid)
    n = len(grid(0))
    table = [[[]*m] * n]

    table[0][0] = grid[0][0]

    for j in range(1, n-1):
        table[0][j] = table[0][j-1] + grid[0][j]

    for i in range(1, m-1):
        table[i][0] = table[i-1][0] + grid[i][0]

    for row in range(1, m-1):
        for col in range(1, n-1):

            table[row][col] = grid[row][col] + max(table[row-1][col], table[row][col-1])


    return table[m-1][n-1]
