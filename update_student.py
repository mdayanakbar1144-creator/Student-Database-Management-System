import sqlite3
from utils import display_students
def updateStudent():
    conn=sqlite3.connect("collage.db")
    cursor = conn.cursor()
    roll_no = int(input("Enter the ROLL NO. : "))
    cursor.execute(""" 
    SELECT * FROM students 
                WHERE roll = ?
                """,(roll_no,))
    result = cursor.fetchone()
    if result is None:
        print("Student not found!")
    else:
        print()
        print("Student detail...")
        display_students(result)
        new_name = input("Enter the new name : ")
        new_branch = input("Enter the new branch : ")
        new_cgpa= float(input("Enter the new CGPA : "))
        print()
        cursor.execute("""
        UPDATE students
                    SET name = ?,
                    branch = ?,
                    cgpa = ?
                    where roll = ?
        """,(new_name,new_branch,new_cgpa,roll_no))
        conn.commit()
        print("Student data is updated successfully!")
        conn.close()
if __name__=="__main__":
    updateStudent()


























