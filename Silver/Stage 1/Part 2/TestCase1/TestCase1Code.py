import string

lines = []
with open('Drifblim.txt') as file:
    for line in file:
        lines.append((line.strip()).lower())

full_text = []
for i in range(len(lines)):
    no_punctuation = lines[i].translate(str.maketrans('', '', string.punctuation)) #Removes punctuation from paragraph
    full_text = full_text + no_punctuation.split(" ") #stores erch individual word seperated by a space in a list

dictionary = {}
for i in range(len(full_text)):
    if full_text[i] not in dictionary:
        dictionary[full_text[i]] = 1
    else:
        dictionary[full_text[i]] = dictionary[full_text[i]] + 1

most_words_count = 0
values = list(dictionary.values())
for i in range(len(values)):
    if values[i] > most_words_count:
        most_words_count = values[i]

print(round(most_words_count/len(dictionary), 3))
