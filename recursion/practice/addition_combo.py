def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    slate = []
    results = []
    arr.sort()
    helper(arr, 0, target, slate, results)
    return results

def helper(nums, idx, target, slate, results):
    #Backtracking
    if target == 0:
        results.append(slate[:])
        return

    #Base Case
    if idx == len(nums) or nums[idx] > target or sum(nums[idx:]) < target:
        return

    #Count
    count = 0
    for val in range(idx, len(nums)):
        if nums[idx] == nums[val]:
            count +=1

    #Recursive
    #include
    slate.append(nums[idx])
    helper(nums, idx+1, target-nums[idx], slate, results)
    slate.pop()

    #exclude
    helper(nums, idx+count, target, slate, results)