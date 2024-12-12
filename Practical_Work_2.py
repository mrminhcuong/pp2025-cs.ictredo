# Set class student mark management system
class System:
  def __init__(self):
    self.__students = []
    self.__courses = []

  # Setter and getter

  def setStudents(self):
    self.__students = []
    for i in range(self.__getInputNum__("students")):
      print("Student " + str(i + 1) + ":")
      self.__students.append(Student())

  def setCourses(self):
    self.__courses = []
    for i in range(self.__getInputNum__("courses")):
      print("Course " + str(i + 1) + ":")
      self.__courses.append(Course())

  def getStudents(self):
    return self.__students

  def getCourses(self):
    return self.__courses

  @staticmethod
  # Enter the number of students
  def __getInputNum__(type_):
    while True:
      try:
        i = int(input("Enter the number of " + type_ + ": "))
        return i
      except ValueError:
        print("Invalid input! Please try again!")
        pass

  # Input course name
  def __getInputCourse__(self):
    while True:
      courseName = input("Enter course name: ")
      for course in self.__courses:
        if courseName == course.getName():
          return course
      print("Invalid course! Try again!")

  # Choose action
  def __getActionId__(self):
    print("==========")
    print("Actions: ")
    print(" (1) List Courses")
    print(" (2) List Students")
    print(" (3) Set Marks (given course)") # Choose only one course
    print(" (4) Get Marks (given course)") # Choose only one course
    print(" (5) Finish")
    while True:
      try:
        i = self.__getInputNum__("Action")
        if i in (1, 2, 3, 4, 5):
          return i
      except ValueError:
        pass
      print("Invalid input! Try again!")

  def __action__(self):
    while True:
      actionId = self.__getActionId__()
      if actionId == 1:
        for course in self.__courses:
          print(course.getName())
      elif actionId == 2:
        for student in self.__students:
          print(student.getName())
      elif actionId == 3:
        course = self.__getInputCourse__()
        course.setMarks(self.__students)
      elif actionId == 4:
        course = self.__getInputCourse__()
        course.getInfo()
      else:
        print("Finish! Thank you!")
        break

  def run(self):
    self.setStudents()
    self.setCourses()
    self.__action__()

class Student:
  # Enter your student information
  def __init__(self):
    self.__id = input("Enter id of Student: ")
    self.__name = input("Enter name of Student: ")
    self.__dob = input("Enter DoB of Student: ")

  # Getter and setter class Student
  def setId(self, id_):
    self.__id = id_

  def setName(self, name_):
    self.__name = name_

  def setDoB(self, dob):
    self.__dob = dob

  def getId(self):
    return self.__id

  def getName(self):
    return self.__name

  def getDoB(self):
    return self.__dob

  def getInfo(self):
    # Print info student
    print("Student: " + self.__name + ":")
    print(" * Id: " + self.__id)
    print(" * Dob: " + self.__dob)

class Course:
  def __init__(self):
    # Input your course
    self.__name = input("Enter Course name: ")
    self.__id = input("Enter Course ID: ")
    self.__marks = []

  # Getter and setter class Course
  def setName(self, name):
    self.__name = name

  def setId(self, id_):
    self.__id = id_

  def setMarks(self, students):
    self.__marks = []
    print("=========")
    for student in students:
      # Caution: Input the mark, you should type float, not int
      mark = float(input("Enter mark of " + student.getName() + ": "))
      self.__marks.append([student.getName(), mark])

  def getName(self):
    return self.__name

  def getId(self):
    return self.__id

  def getMarks(self):
    return self.__marks

  def getInfo(self):
    # Print name Course, ID and mark for this course
    print("Course: " + self.__name + ":")
    print(" * Id: " + self.__id)
    print(" * Marks: ")
    for i in range(len(self.__marks)):
      print("     +   " + self.__marks[i][0] + ": " + str(self.__marks[i][1]))

# Run the code
System = System()
System.run()
