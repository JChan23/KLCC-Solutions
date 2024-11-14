array = [10, 15, 2, 15, 11, 2, 14, 18, 15, 15, 10, 2, 16, 8, 17, 11, 11, 8, 19, 17]
count = 0

for i in range(len(array)):
    if array[i] % 11 == 0:
        count = count + 1

print(count) #unconfirmed output: 3
