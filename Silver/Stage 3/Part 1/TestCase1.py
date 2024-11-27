graveyard = [[15, 7, 17, 14, 11, 16, 14, 11, 2, 7, 12, 19, 4, 7, 17, 3, 20, 17, 17, 11], [5, 13, 8, 8, 9, 13, 20, 5, 10, 18, 1, 14, 16, 14, 15, 19, 2, 6, 6, 3], [13, 14, 4, 6, 18, 20, 1, 20, 15, 15, 20, 20, 13, 20, 9, 16, 18, 4, 19, 2], [17, 8, 19, 6, 14, 9, 8, 2, 15, 12, 3, 12, 8, 6, 20, 20, 13, 4, 13, 8], [12, 18, 9, 17, 17, 9, 14, 1, 9, 13, 9, 7, 4, 4, 6, 3, 1, 7, 2, 19], [9, 16, 19, 5, 11, 6, 8, 5, 4, 5, 7, 2, 8, 4, 10, 18, 3, 1, 8, 6], [14, 20, 3, 19, 4, 20, 6, 15, 11, 15, 20, 19, 18, 6, 6, 18, 15, 7, 19, 12], [6, 20, 7, 12, 9, 18, 18, 15, 15, 14, 19, 15, 12, 6, 6, 19, 13, 19, 15, 1], [4, 20, 20, 18, 6, 3, 14, 16, 9, 19, 17, 16, 18, 1, 13, 9, 3, 2, 11, 7], [17, 15, 10, 18, 16, 7, 12, 13, 15, 10, 16, 3, 16, 13, 1, 6, 1, 13, 6, 2], [5, 19, 11, 9, 17, 14, 20, 10, 13, 15, 12, 6, 10, 14, 17, 6, 18, 15, 4, 7], [1, 20, 13, 18, 18, 1, 17, 5, 16, 20, 4, 15, 9, 1, 3, 9, 20, 10, 17, 9], [2, 1, 8, 13, 10, 13, 15, 12, 16, 18, 1, 17, 3, 17, 17, 18, 20, 4, 7, 9], [19, 7, 14, 5, 10, 8, 14, 14, 17, 10, 9, 7, 13, 18, 18, 3, 11, 5, 15, 7], [10, 5, 11, 17, 14, 5, 12, 11, 3, 17, 17, 11, 3, 8, 14, 12, 5, 10, 5, 17], [16, 3, 8, 13, 20, 1, 20, 6, 19, 16, 16, 13, 1, 20, 16, 10, 20, 15, 10, 12], [17, 4, 13, 5, 3, 2, 4, 6, 19, 20, 3, 9, 7, 9, 5, 6, 20, 17, 4, 5], [4, 10, 7, 12, 19, 9, 9, 4, 8, 6, 15, 6, 4, 15, 12, 14, 20, 13, 7, 5], [17, 18, 9, 8, 16, 11, 19, 15, 11, 1, 19, 18, 15, 8, 5, 11, 8, 3, 13, 5], [12, 10, 7, 20, 5, 12, 3, 1, 14, 5, 12, 9, 1, 7, 6, 6, 8, 7, 5, 7]]
ideal = []

for i in range(len(graveyard)):
    for j in range(len(graveyard[i])):
        if i == 0 and j == 0: #right and under
            if graveyard[i][j] > graveyard[i][j + 1] and graveyard[i][j] < graveyard[i + 1][j]:
                ideal.append((i, j))
        elif i == 0 and j == (len(graveyard[i])-1): #left and under
            if graveyard[i][j] > graveyard[i][j - 1] and graveyard[i][j] < graveyard[i + 1][j]:
                ideal.append((i, j))
        elif i == (len(graveyard)-1) and j == 0: #right and top
            if graveyard[i][j] > graveyard[i][j + 1] and graveyard[i][j] < graveyard[i - 1][j]:
                ideal.append((i, j))
        elif i == (len(graveyard)-1) and j == (len(graveyard[i])-1): #left and top
            if graveyard[i][j] > graveyard[i][j - 1] and graveyard[i][j] < graveyard[i - 1][j]:
                ideal.append((i, j))
        elif i == 0: #left, right and under
            if graveyard[i][j] > graveyard[i][j + 1] and graveyard[i][j] > graveyard[i][j - 1] and graveyard[i][j] < graveyard[i + 1][j]:
                ideal.append((i, j))
        elif j == 0: #top, right and under
            if graveyard[i][j] > graveyard[i][j + 1] and graveyard[i][j] < graveyard[i + 1][j] and graveyard[i][j] < graveyard[i - 1][j]:
                ideal.append((i, j))
        elif i == (len(graveyard)-1): #top, right and left
            if graveyard[i][j] > graveyard[i][j + 1] and graveyard[i][j] > graveyard[i][j - 1] and graveyard[i][j] < graveyard[i - 1][j]:
                ideal.append((i, j))
        elif j == (len(graveyard[i])-1): #under, top and left
            if graveyard[i][j] > graveyard[i][j - 1] and graveyard[i][j] < graveyard[i + 1][j] and graveyard[i][j] < graveyard[i - 1][j]:
                ideal.append((i, j))
        else:
            if graveyard[i][j] > graveyard[i][j + 1] and graveyard[i][j] > graveyard[i][j - 1] and graveyard[i][j] < graveyard[i + 1][j] and graveyard[i][j] < graveyard[i - 1][j]:
                ideal.append((i, j))


print(ideal)
