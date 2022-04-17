from collections import deque

def flood_fill(pixel_row, pixel_column, new_color, image):
    row = len(image)
    col = len(image[0])

    old_color = image[pixel_row][pixel_column]
    image[pixel_row][pixel_column] = new_color
    if old_color == new_color:
        return image

    q = deque([])
    q.append((pixel_row,pixel_column))
    while q:
        i, j = q.popleft()
        if 0<=i-1<row and image[i-1][j] == old_color:
            image[i-1][j] = new_color
            q.append((i-1,j))
        if 0<=i+1<row and image[i+1][j] == old_color:
            image[i+1][j] = new_color
            q.append((i+1,j))
        if 0<=j-1<col and image[i][j-1] == old_color:
            image[i][j-1] = new_color
            q.append((i,j-1))
        if 0<=j+1<col and image[i][j+1] == old_color:
            image[i][j+1] = new_color
            q.append((i,j+1))

    return image