import collections


def count_sort(arr):
    c = collections.Counter(arr)
    result = []
    for i in range(-50000, 50001):
        if i in c:
            for _ in range(c[i]):
                result.append(i)

    return result
