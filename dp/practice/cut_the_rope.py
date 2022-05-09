# Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.
#https://www.geeksforgeeks.org/maximum-product-cutting-dp-36/

def max_product_from_cut_pieces(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    table = [0] * (n+1)

    for i in range(1, n+1):
        largest_prod = 0
        for left_cut in range(1, i):
            right_cut = i - left_cut

            best_right_cut = table[right_cut]

            curr_prod = left_cut * max(right_cut, best_right_cut)

            largest_prod = max(largest_prod, curr_prod)

        table[i] = largest_prod

    return table[n]
