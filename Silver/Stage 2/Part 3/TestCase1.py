N = 100
K = 50
Actions = [(9, 75, 'add'), (56, 87, 'remove'), (81, 91, 'add'), (77, 87, 'remove'), (3, 49, 'add'), (90, 96, 'add'), (87, 91, 'remove'), (85, 98, 'add'), (21, 54, 'add'), (33, 57, 'add'), (28, 56, 'remove'), (41, 68, 'remove'), (17, 97, 'remove'), (55, 76, 'remove'), (97, 98, 'remove'), (22, 78, 'add'), (83, 98, 'remove'), (4, 60, 'remove'), (9, 28, 'remove'), (8, 24, 'remove'), (32, 94, 'remove'), (45, 94, 'remove'), (9, 84, 'remove'), (61, 99, 'add'), (50, 54, 'add'), (97, 98, 'remove'), (97, 100, 'remove'), (79, 98, 'remove'), (46, 60, 'remove'), (39, 79, 'remove'), (18, 38, 'remove'), (7, 93, 'add'), (1, 29, 'remove'), (71, 79, 'add'), (43, 71, 'add'), (58, 94, 'add'), (82, 84, 'remove'), (98, 98, 'remove'), (24, 57, 'add'), (31, 63, 'remove'), (34, 52, 'add'), (80, 83, 'remove'), (91, 99, 'remove'), (88, 93, 'add'), (61, 95, 'remove'), (1, 73, 'remove'), (81, 81, 'add'), (39, 96, 'add'), (78, 79, 'remove'), (31, 32, 'add')]

Bookshelf = []
Final_string = ""

for i in range(N):
    Bookshelf.append("E")

for i in range(K):
    if Actions[i][2] == "add":
        for j in range(Actions[i][0]-1, Actions[i][1]):
            Bookshelf[j] = "B"
    elif Actions[i][2] == "remove":
        for j in range(Actions[i][0]-1, Actions[i][1]):
            Bookshelf[j] = "E"

for i in range(N):
    Final_string = Final_string + Bookshelf[i]

print(Final_string)
