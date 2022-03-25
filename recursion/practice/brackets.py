def generateParenthesis(n):
    result = []
    helper(0, 0, "", n, result)
    return result

def helper(nOpen, nClose, partial, n, result):
    if n == nClose:  # Found a valid n pairs of parentheses
        result.append(partial)
        return

    if nOpen < n:  # Number of opening bracket up to `n`
        helper(nOpen + 1, nClose, partial + "(", n , result)
    if nClose < nOpen:  # Number of closing bracket up to opening bracket
        helper(nOpen, nClose + 1, partial + ")", n, result)

print(generateParenthesis(12))
