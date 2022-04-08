def findTarget(root, k):
    if not root: return False

    stack = [root]
    s = set()
    for curr in stack:
        if k - curr.val in s: return True
        s.add(curr.val)
        if curr.left: stack.append(curr.left)
        if curr.right: stack.append(curr.right)
    return False
