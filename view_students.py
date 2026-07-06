import sqlite3
def view_student():
    conn=sqlite3.connect("collage.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students""")
    students = cursor.fetchall()

    for student in students:
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