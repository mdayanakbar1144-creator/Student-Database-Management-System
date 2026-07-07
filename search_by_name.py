import sqlite3
def lookup_by_name():
    from utils import display_students
    conn=sqlite3.connect("collage.db")
    cursor = conn.cursor()
    target ="%"+ input("Enter tne name : ") + "%"
    cursor.execute(""" 
    SELECT * FROM students
    WHERE name LIKE ?
    """,(target,))
    students = cursor.fetchall()
    if not students:
        print("No students found.")
    for student in students:
        display_students(student)
    conn.close()
if __name__=="__main__":
    lookup_by_name()