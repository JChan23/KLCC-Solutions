array = [0 for i in range(1600001)]
alice_index = 800000
bob_index = 800000

alice = []
with open('Alice.txt') as file:
    for line in file:
        alice.append(line.strip())

bob = []
with open('Bob.txt') as file:
    for line in file:
        bob.append(line.strip())

for i in range(len(alice)):
    move = (alice[i])[0]
    count = 1
    distance = ""
    dirt = ""
    get_dirt = True
    while (alice[i])[count] != " ":
        distance = distance + (alice[i])[count]
        count = count + 1
    distance = int(distance)
    count = count + 1
    try:
        while get_dirt == True:
            dirt = dirt + (alice[i])[count]
            count = count + 1
    except IndexError:
        get_dirt = False
    dirt = int(dirt)

    if move == "L":
        for j in range(distance):
            array[alice_index] = array[alice_index] - dirt
            alice_index = alice_index - 1
        array[alice_index] = array[alice_index] - dirt
    elif move == "R":
        for j in range(distance):
            array[alice_index] = array[alice_index] - dirt
            alice_index = alice_index + 1
        array[alice_index] = array[alice_index] - dirt




for i in range(len(bob)):
    move = (bob[i])[0]
    count = 1
    distance = ""
    dirt = ""
    get_dirt = True
    while (bob[i])[count] != " ":
        distance = distance + (bob[i])[count]
        count = count + 1
    distance = int(distance)
    count = count + 1
    try:
        while get_dirt == True:
            dirt = dirt + (bob[i])[count]
            count = count + 1
    except IndexError:
        get_dirt = False
    dirt = int(dirt)

    if move == "L":
        for j in range(distance):
            array[bob_index] = array[bob_index] + dirt
            bob_index = bob_index - 1
        array[bob_index] = array[bob_index] + dirt
    elif move == "R":
        for j in range(distance):
            array[bob_index] = array[bob_index] + dirt
            bob_index = bob_index + 1
        array[bob_index] = array[bob_index] + dirt


count = 0
for i in range(len(array)):
    if array[i] > 10000:
        count = count + 1

print(count)
