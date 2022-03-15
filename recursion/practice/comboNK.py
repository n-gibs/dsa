def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    helper(n, k, result)
    return result

def helper(n, k, i, partial, result):
    if len(partial) == k:
        result.append(list(partial))
    else:
        for j in range(i+1, n+1):
            partial.append(j)
            helper(n, k, j, partial, result)
            partial.pop()
