import string

original = "Algorithms and data structures are central to computer science. The theory of computation concerns abstract models of computation and general classes of problems that can be solved using them. The fields of cryptography and computer security involve studying the means for secure communication and preventing security vulnerabilities . Computer graphics and computational geometry address the generation of images. Programming language theory considers different ways to describe computational processes, and database theory concerns the management of repositories of data. Human computer interaction investigates the interfaces through which humans and computers interact, and software engineering focuses on the design and principles behind developing software. Areas such as operating systems, networks and embedded systems investigate the principles and design behind complex systems. Computer architecture describes the construction of computer components and computer operated equipment. Artificial intelligence and machine learning aim to synthesize goal orientated processes such as problem solving, decision making, environmental adaptation, planning and learning found in humans and animals. Within artificial intelligence, computer vision aims to understand and process image and video data, while natural language processing aims to understand and process textual and linguistic data."
no_punctuation = original.translate(str.maketrans('', '', string.punctuation)) #Removes punctuation from paragraph
paragraph = no_punctuation.split(" ") #stores erch individual word seperated by a space in a list

longest_word = ""
for i in range(len(paragraph)):
    if len(paragraph[i]) > len(longest_word):
        longest_word = paragraph[i]

print(longest_word)
