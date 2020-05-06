#by using namedtuple storing marks of students and print the average value of marks

from collections import namedtuple
  Point = namedtuple('Point',['Marks']) 
  N=int(input("enter number of students"))
  marks=input().split()
for i in range(len(marks)):
    marks[i] = int(marks[i])
avg= sum(marks)/len(marks)
print('%.2f'%avg)

#by using collections(namedtuple) stroing and printing average marks of student

from collections import namedtuple
   N, Student = int(input()), namedtuple('Student', input().split())
   sl = [Student(*input().split()) for i in range(N)]
   print('%.2f' % (sum([int(student.MARKS) for student in sl])/N))

