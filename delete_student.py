import sqlite3
def deletestudent():
    conn = sqlite3.connect("collage.db")
    cursor = conn.cursor()
    roll_no = int(input("Enter the roll no. : "))
    cursor.execute(""" 
    SELECT * FROM students
                   WHERE roll = ?
    """,(roll_no,))
    student = cursor.fetchone()
    if student is None:
        print("Student not found!")
        conn.close()
        return
    else:
        print()
        print("-" * 30)
        print(f"Roll No  : {student[0]}")
        print(f"Name     : {student[1]}")
        print(f"Age      : {student[2]}")
        print(f"Course   : {student[3]}")
        print(f"Branch   : {student[4]}")
        print(f"Email    : {student[5]}")
        print(f"CGPA     : {student[6]}")
        print("-" * 30)
        print()
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