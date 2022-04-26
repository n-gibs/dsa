#322. Coin Change

#https://leetcode.com/problems/coin-change/

#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

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
