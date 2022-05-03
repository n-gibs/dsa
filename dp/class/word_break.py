#139. word break

#https://leetcode.com/problems/word-break/


#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s)
    table = [False] * (n + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
    table[0] = True
    for i in range(n):
        for j in range(i, n):
            if table[i] and s[i: j+1] in wordDict:
                table[j+1] = True

    return table[-1]