import sqlite3
from utils import display_students,get_student_by_roll_no
def deletestudent():
    conn = sqlite3.connect("collage.db")
    cursor = conn.cursor()
    roll_no = int(input("Enter the roll no. : "))
    student = get_student_by_roll_no(cursor,roll_no)
    if student is None:
        print("Student not found!")
        conn.close()
        return
    else:
        display_students(student)
        choice = input("Are you sure you want to delete this data (Y/N) ? ").strip().upper()       #.Strip removes the ectra spaces given in the input (eg. " y"," Y", "y ",etc.) 
        if choice=="Y":
            cursor.execute("""
DELETE FROM students
                           WHERE roll=?
""",(roll_no,))
            print("Student deleted successfully!")
            conn.commit()
        elif choice=="N":
            print("Deletion cancelled.")
        else:
            print("Invalid choice!!!")
    conn.close()
if __name__=="__main__":
    deletestudent()