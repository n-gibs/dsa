def permutations(s):
    result = []
    helper([], s, result)
    return result

def helper(slate, s, result):
    if len(s) == 0:
        result.append("".join(slate))
        print(result)
        return

    for i in range(len(s)):
        slate.append(s[i])
        print(i, slate, s[:i]+s[i+1:], result)
        helper(slate, s[:i]+s[i+1:], result)
        slate.pop()

print(permutations("123"))
