class Student:

  def  __init__(self,name,roll_number,cgpa):
         self.name = name
         self. roll_number = roll_number
         self.cgpa = cgpa


def sort_students(student_list):

   sorted_students = sorted(student_list,
       key=lambda student: student.cgpa,
      reverse=True)
   return  sorted_students


students  = [
  Student("Ayisha","A12",6.1),
  Student("Shahin","A13",6.2),
  Student ("Nishidha","A14",6.3),
  Student ("karishma","A15",6.4),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {},Roll number:{},CGPA: {}". format(student.name,

student.roll_number,                
                                                        student.cgpa))


