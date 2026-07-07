import sqlite3

def display_students(order_by):
    conn = sqlite3.connect("collage.db")  
    cursor = conn.cursor()

    query = f"""
        SELECT roll, name, cgpa
        FROM students
        ORDER BY {order_by}
    """
    cursor.execute(query)
    students = cursor.fetchall()

    print("\n========== Student List ==========")
    print(f"{'Roll No':<10} {'Name':<20} {'CGPA':<5}")
    print("-" * 40)

    for student in students:
        roll, name, cgpa = student
        print(f"{roll:<10} {name:<20} {cgpa:<5}")
    print("-" * 40)

    conn.close()


def sort_students_menu():
    while True:
        print("\n\n========== Sort Students ==========\n")
        print("1. By Name (A-Z)\n")
        print("2. By Name (Z-A)\n")
        print("3. By CGPA (Highest First)\n")
        print("4. By CGPA (Lowest Fi+rst)\n")
        print("5. By Roll Number\n")
        print("6. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_students("name ASC")

        elif choice == "2":
            display_students("name DESC")

        elif choice == "3":
            display_students("cgpa DESC")

        elif choice == "4":
            display_students("cgpa ASC")

        elif choice == "5":
            display_students("roll ASC")

        elif choice == "6":
            print("Going back...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__=="__main__":
    sort_students_menu()