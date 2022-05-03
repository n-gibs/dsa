#120. Triangle]

#https://leetcode.com/problems/triangle/

#Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

#Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

def min_path(triangle):

    # table = [[0]*i for i in range(1, len(triangle)+1)]

    # table = [0] * (len(triangle) + 1)

    # table[0][0] = triangle[0][0]

    n=len(triangle)
    if n==1:
        return triangle[0][0]

    for row in range(1, n):
        for col in range(0, row +1):
            if col ==0:
                triangle[row][0]+=triangle[row-1][0]
            elif col == row:
                triangle[row][col] += triangle[row-1][-1]
            else:
                triangle[row][col] += min(triangle[row-1][col], triangle[row-1][col-1])


    return min(triangle[-1])
