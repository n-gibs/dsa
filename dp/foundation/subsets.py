def c(n, k):

    if k == 0 or k == n: return 1

    table = [[[] * n] * k]

    for row in range(n):
        table[row][0] = 1

    for col in range(k):
        table[col][col] = 1

    for row in range(2, n):
        for col in range(1, min(row, k)):
            table[row][col] = table[row-1][col] + table[row-1][col-1]


    return table[n-1][k-1]