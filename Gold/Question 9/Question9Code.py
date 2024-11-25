#perform pip install pillow and pip install numpy

from PIL import Image
#water = (0, 128, 255)
#land = (144, 235, 144)
#pixel format: (column, row)

n = 18
matrix = [[-1 for _ in range(256)] for _ in range(256)]
img = Image.open('KLCC-map.png')

for i in range(256):
    for j in range(256):
        pixel = img.getpixel((j, i))
        if pixel == (0, 128, 255):
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

def q9(matrix, n):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or matrix[r][c] == 0:
            return 0
        visited[r][c] = True
        size = 1
        size += dfs(r + 1, c)
        size += dfs(r - 1, c)
        size += dfs(r, c + 1)
        size += dfs(r, c - 1)
        return size

    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                island_size = dfs(r, c)
                if island_size > n:
                    count += 1

    return count

print(q9(matrix, n))
