import string

lines = []
with open('Dark_and_Spooky.txt', encoding="utf8") as file:  # specify encoding to avoid error when removing punctuation
    for line in file:
        lines.append(line.strip())

full_text = []
for i in range(len(lines)):
    no_punctuation = lines[i].translate(str.maketrans('', '', string.punctuation)) #Removes punctuation from paragraph
    no_punctuation = no_punctuation.replace("“", "") # removes quotation marks
    no_punctuation = no_punctuation.replace("”", "") # removes quotation marks
    full_text = full_text + no_punctuation.split(" ") #stores erch individual word seperated by a space in a list

num_of_asterisks = 0
for i in range(len(full_text)):
    if full_text[i] == "dark" or full_text[i] == "ghost" or full_text[i] == "spooky":
        num_of_asterisks = num_of_asterisks + 2  # 2 asterisks par target word in the file

print(num_of_asterisks)
