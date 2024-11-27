array = [-2, 0, 2, 9, -3, 4, 5, 8, 6, 4]
sum = 0

for i in range(len(array)):
    if array[i] > 0:
        sum = sum + array[i]

print(sum)
