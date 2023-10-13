class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
students = [
  Student("Sona", "A101", 3.8),
  Student("suba", "B102", 3.6),
  Student("jeya sri", "C103", 3.9),
  Student("vihasini", "D104", 3.5),
]

sorted_students = sort_students(students)

# Printing the sorted list of students
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
