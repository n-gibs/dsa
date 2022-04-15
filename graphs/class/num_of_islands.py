#num islands
#is graph problem?
    #connecting ajacent lands, horizontal and vertically
    # yes 2d grid map
    # each cell is node and edges betwen up down left gith

# what teaversal?
 #count components
 # bfs to spread out and build the full island

# what extensions?
    # 2d grid dealing wiht 2d coordinates 1/j

# code is up
    # build graph to get neighbors?
    #no we csn get neighbors by checking up down left right

    #outer loop? mutiple traversals
        #yes
    #code base BFS, then extension (getting neighbor is diferernt)

from collections import deque

def count_islands(matrix):

    numrows = len(matrix)
    numcols = len(matrix[0])

    num_islands = 0

    total = 0
    for row in range(numrows):
        total += sum(matrix[row])
    if total == numrows * numcols: return 1

    def get_neighbors(row,column):
            neighbors = []
            up1 = row -1
            if up1 >= 0 and matrix[up1][column] == 1:
                neighbors.append((up1,column))

            down1 = row+1
            if down1 < numrows and matrix[down1][column] == 1:
                neighbors.append((down1,column))

            right1 = column +1
            if right1 < numcols and matrix[row][right1] == 1:
                neighbors.append((row,right1))

            left1 = column -1
            if left1 >= 0 and matrix[row][left1] == 1:
                neighbors.append((row,left1))

            if up1 >= 0 and left1 >= 0 and matrix[up1][left1] == 1:
                neighbors.append((up1,left1))
            if up1 >= 0 and right1 < numcols and matrix[up1][right1] == 1:
                neighbors.append((up1,right1))
            if down1 < numrows and left1 >= 0 and matrix[down1][left1] == 1:
                neighbors.append((down1,left1))
            if down1 < numrows and right1 < numcols and matrix[down1][right1] == 1:
                neighbors.append((down1,right1))
            return neighbors

    def bfs(row,col):
        q = deque()
        q.append((row,col))
        matrix[row][col] = 0

        while q:
            (curr_row,curr_col) = q.popleft()
            neighbors = get_neighbors(curr_row,curr_col)
            for (n_r,n_c) in neighbors:
                if matrix[n_r][n_c] == 1:
                    q.append((n_r,n_c))
                    matrix[n_r][n_c] = 0

    for i in range(numrows):
        for j in range(numcols):
            if matrix[i][j] == 1:
                bfs(i,j)
                num_islands += 1

    return num_islands
