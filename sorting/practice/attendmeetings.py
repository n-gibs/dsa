import heapq
def can_attend_all_meetings(intervals):
    if not intervals:
        return 1
    heapq.heapify(intervals)
    first = heapq.heappop(intervals)

    while intervals:
        current = heapq.heappop(intervals)
        if current[0] >= first[1]:
            first = current
        else:
            return 0
    return 1

a = [[1, 5], [5, 8], [10, 15]]
result = can_attend_all_meetings(a)
assert result == 1
print(result)
