Start = 10
End = 51
harshad = []

for i in range(Start, End+1):
    total = 0
    num = str(i)
    for j in range(len(num)):
        total = total + int(num[j])
    if (i/total) % 1 == 0:
        harshad.append(i)

print(sum(harshad))
