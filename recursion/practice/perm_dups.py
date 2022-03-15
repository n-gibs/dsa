def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []

    def helper(slate, i):
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
                helper(slate, i + 1)
                #swap back
                slate[p], slate[i] = slate[i], slate[p]

    helper(arr, 0)
    return result


print(get_permutations([1,1,2]))