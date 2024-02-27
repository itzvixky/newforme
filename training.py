students = []

n = int(input("Enter Your Student's Strength:"))

for i in range(n):
    name = input("Enter student name:")
    grade = float(input("Enter student grade:"))
    
    students.append([name,grade])
    
students.sort(key=lambda x : x[1])
print(1)
second_lowest_grade = None

for i in range(1,n+1):
   if students[i][1] > students[0][1]:
    second_lowest_grade = students[i][1]   
    break
print(2)
student_name = []
for i in students:
    if i[1] == second_lowest_grade:
       student_name.append(i[0] ) 
print(3)
student_name.sort()
print(4)
for name in student_name:
    print(name)
print(5)