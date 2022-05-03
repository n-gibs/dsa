#118. Pascal's Triangle

#https://leetcode.com/problems/pascals-triangle/

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# #Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def create_triangle(numRows):

    table = [[1]*i for i in range(1, numRows+1)]

    for row in range(2, numRows):
        for col in range(1, row):
            print(table[row-1][col] + table[row-1][col-1])

            table[row][col] = table[row-1][col] + table[row-1][col-1]
            print(table[row][col])

    return table
print(create_triangle(5))
