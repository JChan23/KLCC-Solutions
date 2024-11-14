dictionary = {}
string = "NTRTRAJ87RQ9V9PBLGQ3DRN5IHXJMZU7LITS4EY34J1KX69AU29ZZZAPHAETWQ6XUS12QA4H3XDQ236K9LNR80HA0GPOHAQYT2B895SMPDGILUGCNZCQH26M9AZIAQVOL0TDCDCUBA580NIMKY1174NEC6Z1POXZNXUQ2Y3BMXCRO566HKJ7MR7NP55SXIEPR97TWQIL"

for i in range(len(string)):
    if string[i] not in dictionary:
        dictionary[string[i]] = 1
    else:
        dictionary[string[i]] = dictionary[string[i]] + 1

largest = 0
smallest = 9999999
values = list(dictionary.values())

for i in range(len(values)):
    if values[i] > largest:
        largest = values[i]
    if values[i] < smallest:
        smallest = values[i]

print(largest-smallest) #unconfirmed output: 8
