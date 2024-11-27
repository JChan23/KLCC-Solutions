array = [22, 35, 5, -7, -25, -2, 31, -40, -33, -1, 36, -18, -11, 33, -47, 48, -20, -24, 41, -43, 8, 9, 12, 14, 50]
sum = 0

for i in range(len(array)):
    if array[i] % 2 == 0:
        sum = sum + array[i]

print(sum)
