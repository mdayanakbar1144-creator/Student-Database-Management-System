import sqlite3
# writing statistics query
def statistics_query():
    conn=sqlite3.connect("collage.db")
    cursor=conn.cursor()
    cursor.execute("""
    SELECT COUNT(*),
            AVG (cgpa),
            MAX (cgpa),
            MIN (cgpa)
    FROM students
    """)
    count,avg_cgpa,max_cgpa,min_cgpa = cursor.fetchone()
    conn.close()
    return count,avg_cgpa,max_cgpa,min_cgpa

# Writing query to get the details of stuent by cgpa
def get_student_by_cgpa(cgpa):
    conn=sqlite3.connect("collage.db")
    cursor=conn.cursor()
    cursor.execute("""
SELECT roll,name,course,branch,cgpa FROM students
                   WHERE cgpa = ?
                   ORDER BY roll
""",(cgpa,))
    students = cursor.fetchall()
    conn.close()
    return students

# TO PRINT the students with the same cgpa
def print_students_by_cgpa(students):
    print('-'*72)
    print(f"{'ROLL NO.':<10} {'NAME':<20} {'COURSE':<12} {'BRANCH':<12} {'CGPA':<6}")
    print('-'*72)
    for roll, name,course, branch, cgpa in students:
        print(f"{roll:<10} {name:<20} {course:<12} {branch:<12} {cgpa:.2f}")
    print('-'*72)
    input("Press ENTER to continue...")

# Styling the print value
def print_stylish_value(value):
    print("\n" + "=" * 42)
    print("        STUDENT STATISTICS")
    print("=" * 42)
    print(f"\n{value}")
    print("\n" + "=" * 42)
    input("Press ENTER to continue...")

# To get the stats of the students
def show_stats(stat):
    count,avg_cgpa,_,_= statistics_query()
    if count ==0:
        print("No student records found.")
        return
    elif stat == "count":
        print_stylish_value(f"📊 Total students : {count}") 
    elif stat=="average":
        print_stylish_value(f"🎓 Average cgpa = {avg_cgpa:.2f}")

# To get the maximum cgpa and return all the students of the highest cgpa
def show_student_cgpa(title,index):
    count,_,max_cgpa,min_cgpa=statistics_query()
    if count ==0:
        print("No student records found. ")
        return
    elif index=="max":
        cgpa = max_cgpa
    elif index=="min":
        cgpa=min_cgpa
    print(f"\n========== {title} CGPA ==========\n")
    print(f"{title} CGPA : {cgpa:.2f}\n")
    print("Students...")
    print_students_by_cgpa(get_student_by_cgpa(cgpa))

# User dashboard
def statistic_dashboard():
    while True:
        print("\n========== Statistics Dashboard ==========\n")
        print("1. Total Students. \n")
        print("2. Average CGPA. \n")
        print("3. Highest CGPA. \n")
        print("4. Lowest CGPA. \n")
        print("5. Back \n")
        choice= input("Enter your choice : ")

        if choice =="1":
            show_stats("count")
        elif choice=="2":
            show_stats("average")
        elif choice == "3":
            show_student_cgpa("Maximum","max")
        elif choice == "4":
            show_student_cgpa("Minimum","min")
        elif choice=="5":
            print("Going back...")
            break
        else:
            print("\nINVALID choice! Enter the numbers between 1 to 5")
if __name__=="__main__":
    statistic_dashboard()

