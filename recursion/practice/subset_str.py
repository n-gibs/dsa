#include/ exclude

def subsets(s):
    results = []
    rec(0, [], s, results)

    return results

def rec(idx_sub, partial, s, results):
    if len(s) == idx_sub:
        print(partial)
        results.append("".join(partial))
        return

    #exclude
    rec(idx_sub + 1, partial, s, results)

    #include
    partial.append(s[idx_sub])
    rec(idx_sub + 1, partial, s, results)
    partial.pop()



res = subsets("abc")
print(res)
