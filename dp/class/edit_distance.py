#76. edit distance

#https://leetcode.com/problems/edit-distance/

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character


def min_distance(w1, w2):
    m = len(w1)
    n = len(w2)
    table = [[-1] * (m+1)]*(n+1)

    for i in range(n, -1, -1):
        for j in range(m, -1 , -1):

            if i == n:
                table[i][j] = m-j
                continue
            if j ==m:
                table[i][j] = n-i
                continue

            replace = 1
            if w1[i] == w1[j]:
                replace = 0

            table[i][j] = min(table[i+1][j+1] + replace, table[i][j+1]+1, table[i+1][j]+1)

    return table[0][0]
