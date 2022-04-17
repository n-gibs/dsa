from collections import deque

def max_island_size(grid):

    rows=len(grid)
    cols=len(grid[0])
    if sum(sum(grid[i]) for i in range(rows)) == rows*cols:
        return rows*cols

    def find_neighbours(i,j):
        neighbors=[]
        upper_valid = True if i-1>=0 else False
        lower_valid= True if i+1<rows else False
        right_valid= True if j+1<cols else False
        left_valid = True if j-1>=0 else False

        if upper_valid:
            if grid[i-1][j]==1:
                neighbors.append((i-1,j))

        if lower_valid:
            if grid[i+1][j]==1:
                neighbors.append((i+1,j))

        if right_valid:
            if grid[i][j+1]==1:
                neighbors.append((i,j+1))

        if left_valid:
            if grid[i][j-1]==1:
                neighbors.append((i,j-1))

        return neighbors

    def bfs (node):
        q=deque()
        q.append(node)
        i1,j1=node
        grid[i1][j1]=0
        island_size=0
        while q:
            i1,j1=q.popleft()
            island_size+=1
            for neighbor in find_neighbours(i1,j1):
                k,l=neighbor
                grid[k][l]=0
                q.append(neighbor)
        return island_size

    largest_island=0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                node=(i,j)
                current_size=bfs(node)
                largest_island=max(largest_island,current_size)
    return largest_island
