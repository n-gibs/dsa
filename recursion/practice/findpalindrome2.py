def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    helper(1, [s[0]], s, result)
    return result

def is_pal(slate):
    ele = len(slate)-1
    temp = []
    print(ele)
    while slate[ele] != "|" and ele >= 0:
        temp.append(slate[ele])
        ele -= 1
    if temp == temp[::-1]:
        return True
    else:
        return False

def helper (i, partial, s, result):
    if i == len(s):
        if is_pal(partial):
            result.append("".join(partial))
        return
    else:
        partial.append(s[i])
        helper(i+1, partial, s, result)
        partial.pop()

        if not is_pal(partial):
            return

        partial.extend(["|", s[i]])
        helper(i+1, partial, s, result)
        partial.pop()
        partial.pop()
        return



print(generate_palindromic_decompositions('abba'))
