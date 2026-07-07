import sqlite3
choice_dictionary = {
    "1": "name ASC",
    "2": "name DESC",
    "3": "cgpa DESC",
    "4": "cgpa ASC",
    "5": "roll ASC"
}

def show_sorted_students(order_by):
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
        print("4. By CGPA (Lowest First)\n")
        print("5. By Roll Number\n")
        print("6. Back")

        choice = input("\nEnter your choice: ")

        if choice in choice_dictionary:
            show_sorted_students(choice_dictionary[choice])
        elif choice == "6":
            print("Going back...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__=="__main__":
    sort_students_menu()