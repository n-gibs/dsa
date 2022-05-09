def can_reach_last_house(maximum_jump_lengths):
    """
    Args:
     maximum_jump_lengths(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    n = len(maximum_jump_lengths)
    lastIdx = n-1

    for pos in range(n-1, -1, -1):
        if pos+maximum_jump_lengths[pos] >= lastIdx:
            lastIdx = pos

    return lastIdx == 0
