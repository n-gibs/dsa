def sumEvenGrandparent(root):
    answer = 0
    dfs(root, None, None, answer)
    return answer

def dfs(node, parent, grandParent, answer):
    if not node:
        return
    if parent and grandParent and grandParent.val % 2 == 0:
        answer += node.val
    dfs(node.left, node, parent, answer)
    dfs(node.right, node, parent, answer)
