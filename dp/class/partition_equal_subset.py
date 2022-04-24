from re import L


def partition(nums):
    all_sum = sum(nums)


    if all_sum %2 != 0:
        return False

    half = int(all_sum/2)
    table = [[False] * (half+1)] * len(nums)+1

    for i in range(len(nums) -1, -1): # iterates decreaseing
        for s in range(half+1): #iterate increasing
            # sum is 0
            #first column
            if s == 0:
                table[i][0] = True
                continue

            #bottom row (i is length of nums)
            if i == len(nums):
                table[i][s] = False
                continue

            #current sum is > num at i
            if s >= nums[i]:
                table[i][s] = table[i+1][s-nums[i]]

            table[i][s] = table[i][s] or table[i+1][s]

    return table[0][half]
