import statistics

array = [84.8, 80.4, 70.7, 77.3, 23.7, 55.6, 42.3, 7.9, 6.6, 41.7, 54.4, 24.3, 61.6, 92.5, 11.5, 64.9, 58.8, 57.4, 3.1, 95.0, 56.7, 27.1, 74.5, 3.6, 61.5, 24.9, 28.8, 96.0, 42.1, 82.7, 17.0, 25.5, 2.1, 42.7, 58.8, 44.2, 55.9, 45.7, 25.2, 97.6, 3.3, 21.0, 86.9, 46.8, 79.8, 80.0, 9.3, 78.3, 73.6, 12.6]
print(statistics.median(array))

#Output is 50.599999999999994 due to foating point errors.
#However, since all numbers in the array are to 1 decimal place, our final answer will also be to one decimal place.
#Looking at 50.5999...., it is plausible to determine our answer is 50.6 (which is indeed the correct answer)
