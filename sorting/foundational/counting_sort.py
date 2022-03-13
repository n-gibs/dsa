import collections


def count_sort(arr):
    c = collections.Counter(arr)
    result = []
    for i in range(-50000, 50001):
        if i in c:
            for _ in range(c[i]):
                result.append(i)

    return result

### TESTS ###
a = [14, 2, 8, 3, 5, 45, 6, 12]
result = count_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = count_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = count_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = count_sort(a)
assert result == [2, 14]

a = [2]
result = count_sort(a)
assert result == [2]

a = []
result = count_sort(a)