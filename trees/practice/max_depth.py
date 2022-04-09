class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

def maxDepth(root):
    # Base case
    if root == None:
        return 0
    # Depth level of the tree
    depth = 0
        # Loops through children array
    for child in root.children:
        # Compares current depth of depth with a new level of depth
        # Sets the biggest value to variable depth
        depth = max(depth, maxDepth(child)+1)

    return depth