def fib_dp(n):

    table = [None]*3

    table[0] = 0
    table[1] = 1

    for i in range(2, n):
        table[i%3] = table[(i-1)%3] + table[(i-2)%3]

    return table[n%3]