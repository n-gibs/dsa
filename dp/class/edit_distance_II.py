from dataclasses import replace


#76. edit distance

#https://leetcode.com/problems/edit-distance/

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character

def edit_distance(w1, w2):
    m = len(w1)
    n = len(w2)

    table = [[0]*n]*m

    for col in range(1, n+1):
        table[0][col] = col

    for row in range(1, m+1):
        table[row][0] = row

    for row in range(1, m+1):
        for col in range(1, n+1):
            replace = 1
            if w1[row-1] == w2[col-1]:
                replace = 0

            table[row][col]  = min(table[row-1][col]+1, table[row][col-1]+1, table[row-1][col-1]+replace)

    return table[-1][-1]
    #last element