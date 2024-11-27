CipherText = "Nxwmtkkv Nabmi Nztxcr Cthoqo Edw Xcktch Ccitvh Mwcx"
key = "091879649361182257880105463872979466699296462987886"
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

key_array = []
for i in range(len(key)):
    key_array.append(int(key[i]))

PlainText = ''
count = 0
index = 0
for i in range(len(CipherText)):
    if CipherText[i].isupper() == True and CipherText[i] != " ":
        for j in range(len(upper)):
            if upper[j] == CipherText[i]:
                index = j
                break
        index = (index - key_array[count]) % 26
        PlainText = PlainText + upper[index]
    elif CipherText[i].islower() == True and CipherText[i] != " ":
        for j in range(len(lower)):
            if lower[j] == CipherText[i]:
                index = j
                break
        index = (index - key_array[count]) % 26
        PlainText = PlainText + lower[index]
    else:
        PlainText = PlainText + " "
    count = count + 1

print(PlainText)
