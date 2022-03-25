def nqueens(n):
#fill in the blanks problem
#permutation problem(order matters)
#n blanks to be filled in
    result = []
    helper(0, n, [], result)
    return result

def helper(i, n, partial, result):

    #backtracking
    lastq = len(partial)-1
    for earilerq in range(lastq-1):
        if partial[earilerq] == partial[lastq]:
            return

        rowdiff = abs(lastq - earilerq)
        coldiff = abs(partial[lastq] - partial[earilerq])
        if rowdiff == coldiff:
            return

    if i == n:
        result.append(partial[:])
        return

    #recursive
    for col in range(n-1):
        #queen i to be place in column = col
        partial.append(col)
        helper(i+1, n, partial, result)
        partial.pop()


print(nqueens(3))