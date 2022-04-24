#same as fib but start at 1 (1 and 2 are base case)
def stairs(n):

    if n == 1 or n == 2: return n

    table = [None]*3

    for i in range(3, n):
        table[i%3] = table[(i-1)%3] + table[(i-2)%3]

    return table[n%3]