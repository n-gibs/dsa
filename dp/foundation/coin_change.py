import math

def min_coins(amt, coins):

    table = [math.inf] * (amt+1)

    table[0] = 0

    for i in range(1, amt):
        #look at all coins
        for c in coins:
            if i-c >=0:
                table[i] = min(table[i-c], table[i])

        table[i]+=1

    if table[amt] == math.inf: return -1

    return table[amt]
