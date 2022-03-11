def dutch_flag_sort(balls):

    begin, mid, end = 0, 0, len(balls)-1

    #hoares
    while mid <= end:
        if balls[mid] == "R":
            balls[begin], balls[mid] = balls[mid], balls[begin]
            begin += 1
            mid += 1

        elif balls[mid] == "G":
            mid += 1

        else:
            balls[end], balls[mid] = balls[mid], balls[end]
            end -= 1

    return balls


balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
result = dutch_flag_sort(balls)
assert result  == ["R", "R", "G", "G", "G", "G", "B", "B"]

def flag2(arr):

    #lumotos
    i = 0
    r = g = -1

    while i < len(arr):
        if arr[i] == "G":
            g+=1
            arr[g], arr[i] = arr[i], arr[g]

        elif arr[i] == "R":
            g += 1
            arr[g], arr[i] = arr[i], arr[g]
            r += 1
            arr[r], arr[g] = arr[g], arr[r]

        i+=1

    return arr


balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
result =flag2(balls)
assert result  == ["R", "R", "G", "G", "G", "G", "B", "B"]
