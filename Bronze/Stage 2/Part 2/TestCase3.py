array = [38, 38, 6, 23, 32, 9, 24, 25, 15, 7, 23, 26, 20, 7, 10, 28, 29, 37, 25, 11, 28, 33, 19, 9, 23, 35, 37, 23, 9, 20, 35, 30, 5, 9, 29, 31, 21, 9, 26, 20, 3, 39, 9, 8, 3, 10, 20, 19, 31, 13, 12, 8, 26, 14, 16, 29, 34, 25, 21, 16, 36, 5, 39, 6, 22, 37, 25, 9, 28, 33, 4, 11, 22, 0, 12, 1, 30, 25, 2, 17, 17, 8, 28, 30, 16, 27, 18, 7, 15, 23, 35, 32, 38, 3, 37, 33, 27, 31, 8, 6, 21, 32, 21, 14, 9]
no_duplicates = []

for i in range(len(array)):
    if array[i] not in no_duplicates:
        no_duplicates.append(array[i])

print(no_duplicates)
# The "list(set(array))" method will not work for this test case, as "set()" will change the order of the list
