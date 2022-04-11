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

def num_islands(map):
    rows = len(map)
    cols = len(map[0])

    #2d arr of -1
    visited = [([-1] * cols) for _ in range(rows)]
    #could create set of corrdiate pairs
    islands = 0
    for i in rows:
        for j in cols:
            if visited[i][j] == -1 and map[i][j] == 1:
                bfs(i,j)
                islands+=1


    def bfs(i, j):
        queue = [[i, j]]
        visited[i][j] = 1

        while queue:
            for n_i, n_j in get_neighbors(i, j):
                if visited[n_i][n_j] == -1:
                    visited[n_i][n_j] == 1
                    queue.append[[n_i, n_j]]

    def get_neighbors(i, j):
        #up
        neighbors = []
        if i -1 >= 0 and map[i-1][j] == 1:
            neighbors.append((i-1, j))
        #down
        if i+1 < rows and map[i+1][j]:
            neighbors.append((i+1, j))
        #left
        if j-1 >= 0 and map[i][j-1]:
            neighbors.append((i, j-1))
        #right
        if j+1 < cols and map[i][j+1]:
            neighbors.append((i, j+1))

        return neighbors

    return islands