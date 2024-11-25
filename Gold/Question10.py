X = [2, 1, -1, -2, -2, -1, 1, 2]
Y = [1, 2, 2, 1, -1, -2, -2, -1]
places = []
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(8):
    X_move_1 = X[i]
    Y_move_1 = Y[i]
    for j in range(8):
        X_move_2 = X[j]
        Y_move_2 = Y[j]
        for k in range(8):
            x = 17
            y = 6
            X_move_3 = X[k]
            Y_move_3 = Y[k]
            x = x + X_move_1 + X_move_2 + X_move_3
            y = y + Y_move_1 + Y_move_2 + Y_move_3
            if x > 0 and y > 0:
                places.append((alphabet[y-1], x))

places = list(set(places))
array = []
for i in range(len(places)):
    array.append(places[i][0]+str(places[i][1]))
array.sort()
print(array)
