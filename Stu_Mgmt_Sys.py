class Student:
    def __init__(self,roll_no,name,age,course,marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    def Display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    #create
    def add_student(self):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student = Student(roll_no, name, age, course, marks)
        self.students.append(student)
        print("Student added successfully.")

    #read
    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            student.Display()
            print("-" * 20)

    #update
    def update_student(self):
        roll= int(input("Enter Roll No of the student to update: "))
        for student in self.students:
            if student.roll_no == roll:

                print("Leave blank to keep current value.")

                student.name = input("Enter new Name: ")
                student.age = int(input("Enter new Age: "))
                student.course = input("Enter new Course: ")
                student.marks = float(input("Enter new Marks: "))

                if student.name:
                    student.name = student.name
                if student.age:
                    student.age = int(student.age)
                if student.course:
                    student.course = student.course
                if student.marks:
                    student.marks = float(student.marks)

                print("Student updated successfully.")
                return
        print("Student not found.")
    
    #delete
    def delete_student(self):
        roll=int(input("Enter Roll No of the student to delete: "))
        for student in self.students:
            if student.roll_no==roll:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    #Search
    def search_student(self):
        roll=int(input("Enter Roll No of the student to search: "))
        for student in self.students:
            if student.roll_no==roll:
                print("Student found:")
                student.Display()
                return
        print("Student not found.")

sms=StudentManagementSystem()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        sms.add_student()
    elif choice == '2':
        sms.view_students()
    elif choice == '3':
        sms.update_student()
    elif choice == '4':
        sms.delete_student()
    elif choice == '5':
        sms.search_student()
    elif choice == '6':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")