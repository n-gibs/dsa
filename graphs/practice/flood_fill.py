#733. Flood Fill
#https://leetcode.com/problems/flood-fill/

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.


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