n = 100
guesses = [(73, True), (63, True), (2, True), (41, True), (58, True), (48, True), (34, True), (39, True), (11, True), (21, True), (62, True), (56, True), (100, False), (61, True), (90, False), (37, True), (35, True), (27, True), (18, True), (64, True), (98, False), (72, True), (50, True), (38, True), (78, False), (5, True), (31, True), (13, True), (60, True), (70, True), (75, False), (9, True), (76, False), (15, True), (99, False), (83, False), (17, True), (20, True), (45, True), (23, True), (16, True), (74, False), (28, True), (47, True), (55, True), (54, True), (84, False), (29, True), (33, True), (88, False)]
numbers = []
final_numbers = []

for i in range(1, n+1):
    numbers.append(i)

for i in range(len(guesses)):
    if guesses[i][1] == True:
        for i in range(guesses[i][0]-1):
            numbers[i] = -1
    elif guesses[i][1] == False:
        for i in range(n-1, guesses[i][0]-2, -1):
            numbers[i] = -1

for i in range(len(numbers)):
    if numbers[i] != -1:
        final_numbers.append(numbers[i])

print(final_numbers)
