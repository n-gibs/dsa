def min_cost_stair(stairs):

    n = len(stairs)
    stairs.append(0)
    table = [] * (n +2)
    table[0] = [0]
    table[1] = stairs[0]

    for i in range(2, n+1):
        table[i] = stairs[i-1] + min(table[i-1], table[i-1])

    return table[n+1]
