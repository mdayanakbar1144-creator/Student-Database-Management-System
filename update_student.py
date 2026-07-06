import sqlite3
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
        print("-" * 30)
        print("Student detail...")
        print()
        print(f"ROLL no. : {result[0]}")
        print(f"Name     : {result[1]}")
        print(f"Branch   : {result[4]}")
        print(f"CGPA     : {result[6]}")
        print("-" * 30)
        print()
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


























