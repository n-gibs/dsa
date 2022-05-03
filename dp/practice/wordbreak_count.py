#Word Break Count

# Given a dictionary of words and a string txt, find the number of ways the string can be broken down into the dictionary words. Return the answer modulo 109 + 7.

def work_break_count(dict, text):

    n = len(text)
    words = set(dict)
    lengths = set([len(w) for w in dict])

    counts = [0] * (n+1)

    counts[0] = 1

    for i in range(1, n+1):
        for l in lengths:
            if text[i-l:i] in words:
                counts[i] += counts[i-l]

    return counts[-1] % 1000000007