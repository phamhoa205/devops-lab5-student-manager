
"""
Student Manager — DevOps Lab 5
Module: Main Application
"""

from student import Student


def add_student(students):
    """Thêm sinh viên mới vào danh sách."""
    print("\n--- ADD NEW STUDENT ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")

    student = Student(student_id, name, age, grade)
    students.append(student)

    print("Student added successfully!")


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()
