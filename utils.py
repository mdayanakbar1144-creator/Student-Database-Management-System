def display_students(student):
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
def get_student_by_roll_no(cursor,roll_no):
    cursor.execute(""" 
    SELECT * FROM students
                   WHERE roll = ?
    """,(roll_no,))
    return cursor.fetchone()