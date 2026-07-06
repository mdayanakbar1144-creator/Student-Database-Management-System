import sqlite3
def insert_student():
    conn=sqlite3.connect("collage.db")
    cursor = conn.cursor()
    roll=int(input("Roll no. : "))
    name = input("Name : ")
    age = int(input("Age : "))
    course = input("Course : ")
    branch = input("Branch : ")
    email = input("Email : ")
    cgpa = float(input("CGPA  : "))
    cursor.execute(""" 
    INSERT INTO students
                values(?,?,?,?,?,?,?)
    """,(roll,name,age,course,branch,email,cgpa))
    conn.commit()
    conn.close()

    print("Student data entered successfully!")
if __name__=="__main__":
    insert_student()