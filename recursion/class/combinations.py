def combine(nums, k):
    results = []

    rec(0, [], nums, k, results)

    return results

def rec(idx_subproblem, partial, nums, k, results):
    if len(partial) == k:
        results.append(list(partial))
        return

    if idx_subproblem == len(nums):
        #needed for when prune base case isnt hit in a branch
        return

    rec(idx_subproblem + 1, partial, nums, k, results)

    partial.append(nums[idx_subproblem])
    rec(idx_subproblem + 1, partial, nums, k, results)
    partial.pop()

nums = [1,2,3,5,20]

print(combine(nums, 3))