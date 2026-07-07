import view_students as vs
import insert_student as ist
import lookup_student as ls
import update_student as us
import delete_student as ds
import search_by_name as sn
import sort_student as ss
def main():
    while True:
        print("\n\n ===== Student Database Management System=====\n\n")
        print("1. Add Student. \n")
        print("2. View All Students.\n")
        print("3. Update Data. \n")
        print("4. Delete student.\n")
        print("5. Search Student by Roll number.\n")
        print("6. Search by name.\n ")
        print("7. Sort students.\n ")
        print("8. Exit.\n ")
        choice=input("Enter your choice: ")
        # print()        
        match choice:
            case '1':
                ist.insert_student()
            case '2':
                vs.view_student()
            case '3':
                us.updateStudent()
            case '4':
                ds.deletestudent()
            case "5":
                ls.lookup()
            case "6":
                sn.lookup_by_name()
            case "7":
                ss.sort_students_menu()                
            case '8':
                print("\n\nThanks for using Student database management system :)\n\n")
                break
            case _:
                print("\nThis is an Invalid choice.")
if __name__=="__main__":
    main()
        


