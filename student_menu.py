import view_students as vs
import insert_student as ist
import lookup_student as ls
import update_student as us
import delete_student as ds
def main():
    while True:
        print()
        print(" ===== Student Database Management System=====")
        print("1. Add Student. ")
        print("2. View All Students.")
        print("3. Update Data. ")
        print("4. Delete student.")
        print("5. Search Student by Roll number.")
        print("6. Exit. ")
        choice=input("Enter your choice: ")
        print()

        # if choice=='1':
        #     ist.insert_student()
        # elif choice=='2':
        #     vs.view_student()
        # elif choice=='3':
        #     ls.lookup()
        # elif choice=='4':
        #     print("Thanks for using Student database management system :)")
        #     print()
        #     break
        # else:
        #     print("This is an Invalid choice.")
        
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
            case '6':
                print("Thanks for using Student database management system :)")
                print()
                break
            case _:
                print("This is an Invalid choice.")
if __name__=="__main__":
    main()
        


