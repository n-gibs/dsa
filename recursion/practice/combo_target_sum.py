def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    results = []
    arr = sorted(arr, reverse=True)
    rec(0, [], arr, target, results)
    return results


def rec(idx_subproblem, partial, nums, target, results):

    if sum(partial) == target:
        results.append(list(partial))
        return

    if idx_subproblem == len(nums):
        #needed for when prune base case isnt hit in a branch
        return

    rec(idx_subproblem + 1 , partial, nums, target, results)

    partial.append(nums[idx_subproblem])
    rec(idx_subproblem + 1 , partial, nums, target, results)
    partial.pop()


nums = [1,2,3,5,20]

print(generate_all_combinations(nums, 6))