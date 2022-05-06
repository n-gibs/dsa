from calendar import c


def numberOfPaths(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    MOD = 1000000007
    # if matrix[0][0] == 0 or matrix[rows-1][cols-1] == 0:

    #     return 0
    table = [0] * cols

    for row in rows:
        for col in cols:
            #if matrix pos is 0 then table is 0 as well
            if matrix[row][col] != 1:
                table[col] = 0
            #i way to get from 0,0 to 0,0
            elif row ==0 and col == 0:
                table[col] = 1

            else: #if row ==0 table[col] will be 0
                # if row > 0 use old value in table[col]
                if col > 0:
                    table[col] = table[col] + table[col-1]
                    table[col] = table[col] % MOD


    return table[cols-1]
