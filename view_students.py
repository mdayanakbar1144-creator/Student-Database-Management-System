import sqlite3
from utils import display_students
def view_student():
    conn=sqlite3.connect("collage.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students""")
    students = cursor.fetchall()

    for student in students:
        display_students(student)
    conn.close()
if __name__=="__main__":
    view_student()
    #Better alternative
# import sqlite3
# conn=sqlite3.connect("collage.db")
# conn.row_factory=sqlite3.Row
# cursor = conn.cursor()
# for student in cursor.execute("SELECT * FROM students"):
#     print(student["name"])
#     print(student["cgpa"])
# conn.close()