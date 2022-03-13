def combo(n, k):
    if n <=1 or k == 0 or k == n:
        return 1

    return combo(n-1, k) + combo(n-1, k-1)


print(combo(10, 2))