def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []

    helper([], arr, result)
    return result

def helper(slate, arr, result):
    if len(arr) == 0:
        result.append(list(slate))
        return

    for i in range(len(arr)):
        slate.append(arr[i])
        helper(slate, arr[:i]+arr[i+1:], result)
        slate.pop()


arr = [1, 2, 2]
print(get_permutations(arr))