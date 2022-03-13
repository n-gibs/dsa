#include/ exclude

def subsets(nums):
    results = []
    rec(0, [], nums, results)

    return results

def rec(idx_sub, partial, nums, results):
    if len(nums) == idx_sub:
        results.append(list(partial))
        return

    #exclude
    rec(idx_sub + 1, partial, nums, results)

    #include
    partial.append(nums[idx_sub])
    rec(idx_sub + 1, partial, nums, results)
    partial.pop()



res = subsets([1,2,3,4,5])
print(res)
