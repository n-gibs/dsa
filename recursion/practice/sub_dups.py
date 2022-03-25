def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    nums.sort()
    self.helper(0, [], nums, results)
    return results

def helper(self, idx, partial, nums, results):

    if len(nums) <= idx:
        if partial not in results:
            results.append(partial[:])
        return

    self.helper(idx+1, partial, nums, results)

    partial.append(nums[idx])
    self.helper(idx+1, partial, nums, results)
    partial.pop()
