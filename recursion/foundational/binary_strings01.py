#BFS

def binary_str(n):
    res = ["0", "1"]

    for _ in range(2, n):
        new_res = []
        for s in res:
            new_res.append(s+"0")
            new_res.append(s+"1")
        res = new_res

    return res

print(binary_str(5))