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
    print(result)
    if result:
        return True
    return False

def helper(i, partial, arr, k, result):

    # if i >= len(arr):
    #     if sum(partial) == k:
    #         count+=1
    #     return
    if partial and sum(partial) == k:

        result.append(partial)
        return

    if i == len(arr):
        return

    helper(i+1, partial, arr, k, result)

    partial.append(arr[i])
    helper(i+1, partial, arr, k, result)
    partial.pop()

# def check_if_sum_possible(arr, k):
#     """
#     Args:
#      arr(list_int64)
#      k(int64)
#     Returns:
#      bool
#     """
#     # Write your code here.
#     possible = 0
#     helper(0, [], arr, k, possible)
#     return possible

# def helper(i, partial, arr, k, possible):
#     print(partial, sum(partial))
#     if sum(partial) == k:
#         possible = 1
#         return

#     if i >= len(arr):
#         return

#     helper(i+1, partial, arr, k, possible)

#     partial.append(arr[i])
#     helper(i+1, partial, arr, k, possible)
#     partial.pop()

print(check_if_sum_possible([10, 20], 0))