#recursion
def max_profit(n , P):

    #basecase
    if n == 0: return 0

    result = -1

    for cut in range(1, n+1):
        result = max(result, max_profit(n-cut, P))

    return result

#DP
def max_profit_DP(n, P):

    table = [-1] * (n+1)
    #basecase
    table[0] = P[0]

    for i in range(2, n+1):
        for c in range(1, i+1):
            table[i] = max(table[i], P[c] + table[i-c])
    return table[n]
