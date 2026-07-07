import sqlite3
from utils import display_students,get_student_by_roll_no
def lookup():
    conn=sqlite3.connect("collage.db")
    conn.row_factory=sqlite3.Row
    cursor = conn.cursor()
    roll = int(input("Enter the roll number: "))
    # cursor.execute("""
    # SELECT * FROM students
    #             WHERE roll = ?""",(roll,))
    # result = cursor.fetchone()

    student=get_student_by_roll_no(cursor,roll)
    if student is None:
         print("Student not found!")
    else:
        display_students(student)
    conn.close()
if __name__=="__main__":
    lookup()
        # print()
        # print("-" * 30)
        # print(f"Roll No : {data["roll"]}")
        # print(f"Name    : {data["name"]}")
        # print(f"Age     : {data["age"]}")
        # print(f"Branch  : {data["branch"]}")
        # print(f"Email   : {data["email"]}")
        # print(f"CGPA    : {data["cgpa"]}")
        # print("-" * 30)  
        # print()