def count_ways_to_climb(steps, n):
    """
    Args:
     steps(list_int32)
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    # f(n) = 1+ f(n-step1)+f(n-step2)+....f(n-stepk)
    dp = [0 for _ in range(n+1)]
    dp[0]=1

    for i in range(1,n+1):
        for step in steps:
            if step<=i:
                dp[i] = dp[i]+dp[i-step]

    return dp[-1]