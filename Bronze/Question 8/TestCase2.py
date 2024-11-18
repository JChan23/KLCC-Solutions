array = [5, 8, 12, 5, 7, 12, 15, 8, 19, 22, 5, 7, 23, 25, 26, 27, 19, 30, 31, 8, 33, 35, 36, 25, 37, 38, 39, 40, 41, 33, 42, 43, 44, 45, 46, 30, 47, 48, 49, 50, 51, 52, 53, 54, 45, 55, 56, 57, 58, 59, 60, 61, 33, 63, 64, 65, 66, 67, 45]
no_duplicates = []

for i in range(len(array)):
    if array[i] not in no_duplicates:
        no_duplicates.append(array[i])

print(no_duplicates)
# The "list(set(array))" method will not work for this test case, as "set()" will change the order of the list
