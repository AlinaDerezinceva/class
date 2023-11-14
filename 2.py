class Student:

    def __init__(self,id, name, var, group):
        self.id = id
        self.name = name
        self.var = var
        self.group = group
    
file=open('students.txt','r',encoding='utf-8')
students = []


for student in file:
    s = student.split(';')
    student = Student(s[0], s[1], s[2], s[3])
    students.append(student)
    
print('------------------------------------------------------------')
print('| ID | FIO                               | VARIANT | GROUP |')
print('------------------------------------------------------------')

for student in students:
    student1 = 2 - len(student.id)
    student2 = 35 - len(student.name)
    student3 = 8 - len(student.var)
    student4 = 5 - len(student.group)
    print(f"| {student.id + ' '*student1} | {student.name + ' '*student2} | {student.var + ' '*student3} | {student.group + ' '*student4} |")

print('------------------------------------------------------------')