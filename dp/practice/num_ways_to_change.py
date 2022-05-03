def number_of_ways(coins, amount):
    """
    Args:
     coins(list_int32)
     amount(int32)
    Returns:
     int32
    """
    dp = [0]*(amount+1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amount+1):
            dp[a] = dp[a-coin]+dp[a]

    return dp[amount]%1000000007