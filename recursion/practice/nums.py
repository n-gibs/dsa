def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    helper('', 0, 0, 0, result, target)
    return result


def helper(slate, index, evaluated, prev, result, target):
        if index == len(s):
            if evaluated == target:
                result.append(slate)
            return
        else:
            for i in range(index, len(s)):
                curr = s[index:i+1]
                curr_int = int(curr)
                if index == 0:
                    helper(slate + curr, i+1, curr_int, curr_int, result, target)
                else:
                    helper(
                        slate + '+' +
                        curr, i+1,
                        evaluated+curr_int,
                        curr_int,
                        result,
                        target
                    )
                    helper(
                        slate + '*' +
                        curr, i+1,
                        (evaluated-prev) + (prev*curr_int),
                        prev*curr_int,
                        result,
                        target
                    )


# def intersperse(lst, item):
#     result = [item] * (len(lst) * 2 - 1)
#     result[0::2] = lst
#     return result

s = "202"
t = 4

print(generate_all_expressions(s, t))
