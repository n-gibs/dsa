from collections import deque
def string_transformation(words, start, stop):
    """
    Args:
     words(list_str)
     start(str)
     stop(str)
    Returns:
     list_str
    """
    # Write your code here.
    words_set = set(words)
    visited = {}

    def get_neighbors(target, words_set):
        neighbors = []
        if len(words_set) > 26:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(target)):
                    word = target[:i] + c + target[i + 1:]
                    if word in words_set:
                        neighbors.append(word)
        else:
            for word in words_set:
                count = 0
                for i in range(len(target)):
                    if target[i] != word[i]:
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    neighbors.append(word)
        return neighbors

    def get_distance(word, stop):
        count = 0
        for i in range(len(word)):
            if word[i] != stop[i]:
                count += 1
            if count > 1:
                return count
        return count

    if get_distance(start, stop) == 1:
        return [start, stop]

    def bfs(start):
        que = deque([(start, [start])])
        visited[start] = True
        while len(que) > 0:
            node, trans = que.popleft()
            for neighbor in get_neighbors(node, words_set):
                if get_distance(neighbor, stop) == 1:
                    return trans + [neighbor, stop]

                if neighbor not in visited:
                    visited[neighbor] = True
                    que.append((neighbor, trans + [neighbor]))
        return ["-1"]

    return bfs(start)