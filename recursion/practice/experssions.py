def generate_all_expressions(s, target):
    # create an array to hold the result
    result = []
    helper('',0,0,0, s, target, result)
    return result
def helper(partial,evaluated,index, prev, s, target, result):
    if index ==len(s):
        if evaluated == target:
            result.append(partial)
            return
    else:
        for i in range(index,len(s)):
            curr = s[index:i+1]
            curr_int = int(curr)

            if index == 0:
                #join
                helper(
                    partial+curr,
                    curr_int,
                    i+1,
                    curr_int,
                    s, target, result)
            else:
                print(evaluated+curr_int)
                #addition
                helper(
                    partial+'+'+curr,
                    evaluated+curr_int,
                    i+1,curr_int,
                    s, target, result)
                print((evaluated-prev)+(prev*curr_int))
                #mutiplication
                helper(
                    partial+'*'+curr,
                    (evaluated-prev)+(prev*curr_int),
                    i+1,prev*curr_int,
                    s, target, result)

print(generate_all_expressions("1203", 6))