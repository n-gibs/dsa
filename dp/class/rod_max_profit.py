#Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the locations where the cuts are to be made for maximum profit.

#recursion
def max_profit(n , P):

    #basecase
    if n == 0: return 0

    result = -1

    for cut in range(1, n+1):
        result = max(result, max_profit(n-cut, P))

    return result

#DP
def max_profit_DP(price):

    n = len(price)
    table = [0] * (n + 1)


    for i in range(1, n + 1):
        table[i] = price[i-1]
        for cut in range(1, i):
            table[i] = max(table[i], table[i-cut] + price[cut-1])

    return table[-1]
