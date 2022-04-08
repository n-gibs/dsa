def postTrav(root):
    if root == None:
        return []

    result = []
    stk = []
    stk.append(root)
    while  stk:
        cur = stk[-1]
        if cur.left:
            stk.append(cur.left)
            cur.left = None
        elif cur.right:
            stk.append(cur.right)
            cur.right = None
        else:
            result.append(cur.value)
            stk.pop()
    return result