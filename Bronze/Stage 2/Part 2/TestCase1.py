array = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 3, 9, 10, 4, 11, 12, 6, 13, 14, 15, 8, 16, 17, 18, 9, 19, 20]
no_duplicates = []

for i in range(len(array)):
    if array[i] not in no_duplicates:
        no_duplicates.append(array[i])

print(no_duplicates)

# The "list(set(array))" method will also work for this test case, as the elements of the original list are ordered
