dungeon = [[1, 1, 0, 1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 1, 1, 1, 0, 0]]

most_0s = 0
for index, row in enumerate(dungeon):
    consecutive_0s = 0
    for num in row:
        if num:
            consecutive_0s = consecutive_0s + 1
            if consecutive_0s > most_0s:
                most_0s = consecutive_0s

print(most_0s)
