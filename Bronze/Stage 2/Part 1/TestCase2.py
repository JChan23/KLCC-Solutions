array = [487, -631, 902, -759, 123, -214, 730, -812, 564, 291, -148, 456, 832, -925, 687, -451, 320, -117, 794, 921, -329, 604, -938, 481, -272, 110, 387, -659, 829, -502, 705, -799, 173, 258]
sum = 0

for i in range(len(array)):
    if array[i] % 2 == 0:
        sum = sum + array[i]

print(sum)
