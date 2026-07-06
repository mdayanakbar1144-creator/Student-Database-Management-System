import sqlite3
def lookup():
    conn=sqlite3.connect("collage.db")
    conn.row_factory=sqlite3.Row
    cursor = conn.cursor()
    roll = int(input("Enter the roll number: "))
    # cursor.execute("""
    # SELECT * FROM students
    #             WHERE roll = ?""",(roll,))
    # result = cursor.fetchone()

    for data in cursor.execute("""
    SELECT * FROM students
                WHERE roll = ?""",(roll,)):
        print()
        print("-" * 30)
        print(f"Roll No : {data["roll"]}")
        print(f"Name    : {data["name"]}")
        print(f"Age     : {data["age"]}")
        print(f"Branch  : {data["branch"]}")
        print(f"Email   : {data["email"]}")
        print(f"CGPA    : {data["cgpa"]}")
        print("-" * 30)  
        print()
        break
    else:
        print("Student not found!")  
    conn.close()
if __name__=="__main__":
    lookup()