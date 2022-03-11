def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    arr1.sort()
    arr2.sort()
    arr3.sort()

    new_arr = intersection(arr1, arr2)


    return intersection(arr3, new_arr)


def intersection(arr1, arr2):

    print(arr1, arr2)

    ptr1 = 0
    ptr2 = 0

    common = []

    while ptr1 < len(arr1) and ptr2 < len(arr2):
        print(arr1[ptr1], arr2[ptr2])
        if arr1[ptr1] == arr2[ptr2]:
            common.append(arr1[ptr1])
            ptr1+=1
            ptr2+=1

        elif arr1[ptr1] < arr2[ptr2]:
            ptr1+=1

        elif arr1[ptr1] > arr2[ptr2]:
            ptr2+=1

        else:
            if common[-1] != arr1[ptr1]:
                common.append(arr1[ptr1])
                ptr1+=1
                ptr2+=1

    return common


arr1 =  [2, 5, 10]
arr2 =  [2, 3, 4, 10]
arr3 =  [2, 4, 10]

inter = find_intersection(arr1, arr2, arr3)
print(inter)
