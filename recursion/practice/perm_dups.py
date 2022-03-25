def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    helper(arr, 0, result)
    return result

def helper(slate, i, result):
    if i == len(slate) - 1:
        print(slate[:])
        result.append(slate[:])
        return

    # every time u start filling the left most blank, start with a new 'used' set
    used = {}
    for p in range(i, len(slate)):
        if slate[p] not in used:
            used[slate[p]] = 1
            #swap
            slate[p], slate[i] = slate[i], slate[p]
            helper(slate, i + 1, result)
            #swap back
            slate[p], slate[i] = slate[i], slate[p]




print(get_permutations([1,1,2]))