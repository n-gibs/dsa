def add_seq(n, a, b):

    if n == 0:
        return a

    return add_seq(n-1, b, a+b)

print(add_seq(10, 0, 1))