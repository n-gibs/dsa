#DFS

def helper(slate, n):

    if n == 0:
        return slate

    helper(slate+"0", n-1)
    helper(slate+"1", n-1)

    return slate

def binary_str(n):
    helper("", n)

print(binary_str(5))