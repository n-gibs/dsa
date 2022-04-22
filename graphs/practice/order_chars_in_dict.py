import collections
def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    graph = collections.defaultdict(set)
    alphabets = set([ c for word in words for c in word ])

    for word1, word2 in zip(words, words[1:]):

        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                graph[c2].add(c1)
                break

    ans = []
    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]

        visited[node] = False

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False

        visited[node] = True

        ans.append(node)
        return True

    for c in alphabets:
        if c not in visited:
            if not dfs(c):
                return ''

    return "".join(ans)
