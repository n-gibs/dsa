def check_if_sum_possible_bool(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.

    return helper(0, 0, 0, arr, k)

def helper(i, count, sum, arr, k):

    if sum == k:
        if count != 0:
            return True

    if i == len(arr):
        return False

    left = helper(i+1, count+1, sum+arr[i], arr, k)

    if left:
        return left
    right = helper(i+1, count, sum, arr, k)

    return right

print(check_if_sum_possible_bool([1, 2, 3], 6))


def check_if_sum_possible(arr, k):
    """
    Args:
     arr(list_int64)
     k(int64)
    Returns:
     bool
    """
    # Write your code here.
    result = []
    helper(0, [], arr, k, result)
    return result

def helper(i, partial, arr, k, result):

    if partial and sum(partial) == k:

        result.append(partial)
        return

    if i == len(arr):
        return

    helper(i+1, partial, arr, k, result)

    partial.append(arr[i])
    helper(i+1, partial, arr, k, result)
    partial.pop()