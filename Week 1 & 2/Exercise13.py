# Base class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Teacher class inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}.")


# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")


# YouTuber class inheriting from Person
class YouTuber(Person):
    def __init__(self, name, age, channel):
        super().__init__(name, age)
        self.channel = channel

    def create_content(self):
        print(f"{self.name} is creating content on {self.channel}.")


# Student can become a Teacher
class StudentTeacher(Student, Teacher):
    def __init__(self, name, age, course, subject):
        # Using super to call the constructors of both Student and Teacher classes
        super().__init__(name, age, course)
        Teacher.__init__(self, name, age, subject)


# Someone can be both a Student and a YouTuber
class StudentYouTuber(Student, YouTuber):
    def __init__(self, name, age, course, channel):
        # Using super to call the constructors of both Student and YouTuber classes
        super().__init__(name, age, course)
        YouTuber.__init__(self, name, age, channel)


# Example usage:

# Creating a Teacher
teacher = Teacher("John", 35, "Mathematics")
teacher.teach()

# Creating a Student
student = Student("Alice", 20, "Computer Science")
student.study()

# Student becomes a Teacher (StudentTeacher)
student_teacher = StudentTeacher("Bob", 25, "Physics", "Engineering")
student_teacher.study()
student_teacher.teach()

# Someone can be both a Student and a YouTuber (StudentYouTuber)
student_youtuber = StudentYouTuber("Mike", 22, "English", "Education")
student_youtuber.study()
student_youtuber.create_content()
