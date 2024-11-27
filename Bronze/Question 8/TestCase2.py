import string

original = "They're creepy and they're kooky. Mysterious and spooky. They're all together ooky . The Addams family. Their house is a museum. When people come to see 'em, They really are a screaming. The Addams family. Neat Sweet Petite. So, put a witch's shawl on, A broomstick you can crawl on. We're gonna play a call on. The Addams family. They're creepy and they're kooky. Mysterious and spooky. They're all together ooky. The Addams family. Strange Deranged The Addams family"
no_punctuation = original.translate(str.maketrans('', '', string.punctuation)) #Removes punctuation from paragraph
paragraph = no_punctuation.split(" ") #stores erch individual word seperated by a space in a list

longest_word = ""
for i in range(len(paragraph)):
    if len(paragraph[i]) > len(longest_word):
        longest_word = paragraph[i]

print(longest_word)
