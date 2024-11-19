Student = "CAADACDBDCCCABBBBAACCDDCCCDBACDBCBBDABBBDAABADDBBC"
Answer = "DCDCCADCBBDCBCACBAACABDCADCBABCBBDDCACDDABAABAACCA"
marks = 0
max_marks = 5*len(Answer)

for i in range(len(Student)):
    if Student[i] == Answer[i]:
        marks = marks + 5
    else:
        marks = marks - 1

print(round((marks/max_marks)*100))
