import sqlite3
def student_data():
    conn=sqlite3.connect("collage.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
                roll INTEGER PRIMARY KEY, 
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT,
                branch TEXT,
                email TEXT, 
                cgpa REAL
                )""")
    conn.commit()
    print("Table created successfully!")
    conn.close()
if __name__ =="__main__":
    student_data()