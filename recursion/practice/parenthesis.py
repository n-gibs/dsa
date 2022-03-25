def generateParenthesis(n):
    result = []
    helper(0, 0, "", n, result)
    return result

def helper(left_open, right_close, partial, n, result):
    # if n == right_close:  # Found a valid n pairs of parentheses
    if left_open == right_close and left_open == n:
        result.append(partial)
        return

    if left_open < n:  # Number of opening bracket up to `n`
        helper(left_open + 1, right_close, partial + "(", n , result)
    if right_close < left_open:  # Number of closing bracket up to opening bracket
        helper(left_open, right_close + 1, partial + ")", n, result)

print(generateParenthesis(12))
