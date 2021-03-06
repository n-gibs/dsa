# Min Knight Moves
# https://leetcode.com/problems/minimum-knight-moves/

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

from collections import deque
def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    """
    Args:
     rows(int32)
     cols(int32)
     start_row(int32)
     start_col(int32)
     end_row(int32)
     end_col(int32)
    Returns:
     int32
    """

    if start_row == end_row and start_col == end_col:
        return 0

    moves = 0
    neighbors = [(2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,-2),(-1,2),(-2,1)]
    visited = [[-1] * cols for _ in range(rows)]

    q = deque([])
    q.append((start_row, start_col))
    visited[start_row][start_col] = 1

    while q:
        moves += 1

        for _ in range(len(q)):
            curr_row, curr_col = q.popleft()

            for i, j in neighbors:
                next_row = curr_row+i
                next_col = curr_col+j

                if next_row>=0 and 0<=next_col and next_row < rows and next_col < cols:

                    if visited[next_row][next_col] == -1:
                        visited[next_row][next_col] = 1
                        q.append((next_row, next_col))

                        if next_row==end_row and next_col == end_col:
                            return moves

    return -1