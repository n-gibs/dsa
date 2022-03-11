def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """

    medians = []

    for i in range(0, len(stream)):
        current_arr = stream[0:i+1]
        print(current_arr)
        if len(current_arr) <=1:
            medians.append(current_arr[i])
        elif len(current_arr) % 2 != 0:
            print(current_arr[len(current_arr)//2])
            # current_arr[len(current_arr)]
            medians.append(current_arr[len(current_arr)//2])
        else:
            # print(len(current_arr)//2)
            floor = len(current_arr)//2
            avg = (current_arr[floor] + current_arr[floor - 1]) // 2
            medians.append(avg)
    # Write your code here.
    # if len is odd, take middle umber
    # len is even, take avg of middle 2 nums
    return medians



print(online_median([3, 8, 5, 2]))
