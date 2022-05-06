#198. House Robber


def maximum_stolen_value(values):

    if len(values) <= 2:
        return max(values)

    prev_m = values[0]

    cur_m =values[1]

    i = 2
    while i < len(values):
        new_m = prev_m + values[i]
        if prev_m < cur_m:
            prev_m = cur_m
        cur_m = new_m
        i+=1
    return max(cur_m,prev_m)