#order of characters in alien dictionary

#https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/

# Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

#Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
# Output: Order of characters is 'b', 'd', 'a', 'c'
# Note that words are sorted and in the given language "baa"
# comes before "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.

# Input:  words[] = {"caa", "aaa", "aab"}
# Output: Order of characters is 'c', 'a', 'b'

def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    # Write your code here

    #creating the adj_list

    max_len = 0

    letters = set()
    for j in words:
        for k in j:
            letters.add(k)

    letters = list(letters)

    adj_list = {}
    for i in range(0, len(letters)):
        adj_list[letters[i]] = []

    visited = {}
    for i in range(0, len(letters)):
        visited[letters[i]] = -1

    arrivals = {}
    for i in range(0, len(letters)):
        visited[letters[i]] = -1

    departures = {}
    for i in range(0, len(letters)):
        visited[letters[i]] = -1

    for i in range(0,len(words)-1):

        word1 = list(words[i])
        word2 = list(words[i+1])
        compare = 1
        index = 0


        while compare == 1 and index<min(len(word1), len(word2)):
            if word1[index] != word2[index]:
                adj_list[word1[index]].append(word2[index])
                compare = 0
            else:
                index = index + 1

    #print(adj_list)

    time_stamp = 0

    def dfs(node):
        nonlocal time_stamp
        visited[node] = 1

        time_stamp =+ 1
        arrivals[node] = time_stamp

        for neighbor in adj_list[node]:
            print(neighbor)

            if visited[neighbor] == -1:

                dfs(neighbor)

        time_stamp += 1
        departures[node] = time_stamp

    #print(words[0][0])

    for letter in visited.keys():
        if visited[letter] == -1:
            dfs(letter)

    #print(departures)

    list_ = []

    for i in departures.keys():
        list_.append([i, departures[i]])

    list_.sort(key = lambda x: x[1])

    return_list = []

    for i in list_:
        return_list.append(i[0])

    return_list2 = ''.join(i for i in return_list)

    return return_list2[::-1]