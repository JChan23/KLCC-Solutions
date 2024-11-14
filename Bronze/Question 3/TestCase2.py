dictionary = {}
string = "lLq5KWgbpTxHYMD7IZ6IMn3MHuFrurmjpRGa8CL14EtnFIiIjBeIDIQQ01c2GOQbm1jDoeMiT7xwYkqpptg7zmGH16FoLa1PMg1GAk6kWXNKTRNH4DlMwKYwMWUggxOfRE2ZAERfDRTpCv4WcKXdqV94jYm9IdrVkaQSqjbvhVtfAZBp4G7TcmCUMbwjKRaKMS6d6zW8"

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
