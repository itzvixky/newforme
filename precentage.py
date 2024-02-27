n = int(input())
students = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float,line))
    students[name] = scores
query_stud = input()

marks = ''
for i in students.keys():
    if i == query_stud:
        marks = students[query_stud] 
    break   

mark = 0
for i in marks:
    mark = i + mark
    percentage = mark/len(marks)

print('{:.2f}'.format(percentage))


  
