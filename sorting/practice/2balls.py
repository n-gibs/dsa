def twoballs(arr):

    ##lomuts i and j start at 0
    # hoares i = 0 j = end

    #lomutos
    # decrease and conquer
    i = 0
    r = i-1
    while i < len(arr):
        if arr[i] == "R":
            r +=1
            if r != i:
                arr[i], arr[r] = arr[r], arr[i]
        i += 1

    return arr

balls = ["G", "G", "R", "G", "R", "R", "G"]
result = twoballs(balls)
print(result)
assert result  == ["R", "R", "R", "G", "G", "G", "G"]
