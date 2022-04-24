#76. edit distance
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
