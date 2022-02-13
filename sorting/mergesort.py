from heapq import merge


def helper(A, start, end):
    if start >= end:
        return

    mid = (start+end)//2

    helper(A, start, mid)
    helper(A, mid+1, end)

    #merge 2 sorted halfs

    i = start
    j = mid+1
    aux = []

    while i <= mid and j<= end:
        if A[i] <= A[j]:
            aux.append(A[i])
            i+=1

        else:
            aux.append(A[j])
            j+=1

    while i <= mid:
        aux.append(A[i])
        i+=1

    while j <= end:
        aux.append(A[j])
        j+=1

    A[start:end+1] = aux

def merge_sort(A):

    helper(A, 0, len(A) - 1)

    return A


### TESTS ###
a = [14, 2, 8, 3, 5, 45, 6, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = merge_sort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = merge_sort(a)
assert result == [2, 14]

a = [2]
result = merge_sort(a)
assert result == [2]

a = []
result = merge_sort(a)
assert result == []