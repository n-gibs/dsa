#BFS

def binary_str(n):
    if n == 1:
        return ["0", "1"]

    prev = binary_str(n-1)
    res = []

    for s in prev:
        res.append(s+"0")
        res.append(s+"1")

    return res

print(binary_str(5))