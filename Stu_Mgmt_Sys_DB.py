import mysql.connector


#Database Connection Class
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Lk225@",
            database="student_db"
        )
        self.cursor = self.conn.cursor()

    def execute(self, query, values=None):
        self.cursor.execute(query, values or ())
        self.conn.commit()


# Student Class
class Student:
    def __init__(self, roll_no, name, age, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


# 🔹 Student Management System
class StudentManagementSystem:
    def __init__(self):
        self.db = Database()

    # CREATE
    def add_student(self):
        try:
            roll = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            query = """
            INSERT INTO students (roll_no, name, age, course, marks)
            VALUES (%s, %s, %s, %s, %s)
            """
            self.db.execute(query, (roll, name, age, course, marks))
            print(" Student Added Successfully!")

        except mysql.connector.Error as e:
            print("Database Error:", e)
        except ValueError:
            print("Invalid input")

    # READ
    def view_students(self):
        self.db.cursor.execute("SELECT * FROM students")
        records = self.db.cursor.fetchall()

        if not records:
            print("No students found")
            return

        print("\n--- Student List ---")
        for s in records:
            print(f"Roll:{s[0]}, Name:{s[1]}, Age:{s[2]}, Course:{s[3]}, Marks:{s[4]}")

    # UPDATE
    def update_student(self):
        roll = int(input("Enter Roll No to Update: "))

        query = "UPDATE students SET name=%s, age=%s, course=%s, marks=%s WHERE roll_no=%s"
        name = input("New Name: ")
        age = int(input("New Age: "))
        course = input("New Course: ")
        marks = float(input("New Marks: "))

        self.db.execute(query, (name, age, course, marks, roll))
        print("Student Updated Successfully!")

    # DELETE
    def delete_student(self):
        roll = int(input("Enter Roll No to Delete: "))
        self.db.execute("DELETE FROM students WHERE roll_no=%s", (roll,))
        print("Student Deleted Successfully!")

    #SEARCH
    def search_student(self):
        roll = int(input("Enter Roll No to Search: "))
        self.db.cursor.execute("SELECT * FROM students WHERE roll_no=%s", (roll,))
        s = self.db.cursor.fetchone()

        if s:
            print(f"Roll:{s[0]}, Name:{s[1]}, Age:{s[2]}, Course:{s[3]}, Marks:{s[4]}")
        else:
            print("Student not found")


# MAIN MENU
sms = StudentManagementSystem()

while True:
    print("\n====== Student Management System (MySQL) ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.view_students()
    elif choice == "3":
        sms.update_student()
    elif choice == "4":
        sms.delete_student()
    elif choice == "5":
        sms.search_student()
    elif choice == "6":
        print("👋 Exiting...")
        break
    else:
        print("Invalid choice")
