def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # start from end
    # because extra space is from the end
    i = len(first)-1
    j = len(first)-1
    k = len(second)-1

    while(i >= 0 and j >= 0):
        if first[i] >= second[j]:
            second[k] = first[i]
            i -= 1
        else:
            second[k] = second[j]
            j -= 1
        k -= 1
        print(second)

    while i >= 0:
        second[k] = first[k]
        i -= 1
        k -= 1

    while j >= 0:
        second[k] = second[j]
        j -= 1
        k -= 1

    return second

# "first": [1, 3, 5],
# "second": [2, 4, 6, 0, 0, 0]


res = merge_one_into_another([1, 3, 5], [2, 4, 6, 0, 0, 0])
assert res == [1, 2, 3, 4, 5, 6]
print(res)
