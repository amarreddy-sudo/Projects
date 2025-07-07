import os

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    student = Student(roll, name, marks)
    
    with open("students.txt", "a") as file:
        file.write(str(student) + "\n")
    print("Student added successfully.\n")

def display_students():
    if not os.path.exists("students.txt"):
        print("No student data found.\n")
        return
    print("\nStudent Records:")
    with open("students.txt", "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    print()

def search_student():
    roll = input("Enter Roll No to search: ")
    found = False
    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print(f"Found: Roll: {data[0]}, Name: {data[1]}, Marks: {data[2]}\n")
                found = True
                break
    if not found:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    lines = []
    deleted = False
    with open("students.txt", "r") as file:
        lines = file.readlines()
    with open("students.txt", "w") as file:
        for line in lines:
            if line.startswith(roll + ","):
                deleted = True
                continue
            file.write(line)
    if deleted:
        print("Student deleted.\n")
    else:
        print("Student not found.\n")

def main():
    while True:
        print("===== Student Record System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by Roll No")
        print("4. Delete Student by Roll No")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
