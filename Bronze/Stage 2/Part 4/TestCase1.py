import string

original = "Kuala Lumpur, officially the Federal Territory of Kuala Lumpur, and colloquially referred to as KL, is the capital city and a federal territory of Malaysia. It is the largest city in the country, covering an area of 243 km^2 with a census population of two million as of 2024. Greater Kuala Lumpur, also known as the Klang Valley, is an urban agglomeration of nine million people as of 2024. It is among the fastest growing metropolitan regions in Southeast Asia, both in population and economic development."
no_punctuation = original.translate(str.maketrans('', '', string.punctuation)) #Removes punctuation from paragraph
paragraph = no_punctuation.split(" ") #stores erch individual word seperated by a space in a list

longest_word = ""
for i in range(len(paragraph)):
    if len(paragraph[i]) > len(longest_word):
        longest_word = paragraph[i]

print(longest_word)
