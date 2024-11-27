letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['91', '4', '321', '71', '211', '221', ' ', '612', '841', ' ', '62', ' ', '121', '801', '432', '172', '36', '482', ' ', '901', '27', '19', ' ', '631', '25', '21', '431']
message = ""
reversed = ""
letter_index = -1

for i in range(len(nums)):
    if nums[i] == ' ':
        message = message + ' '
    else:
        reversed = int((nums[i])[::-1])
        letter_index = reversed % 26
        message = message + letters[letter_index]

print(message)
