# On terminal just type------------- pip install mysql-connector-python

from dbhelper import DBHelper
def main():
    db=DBHelper()
    while True:
        print("************************WELCOME (IT's Confidentials)*************************************")
        print()
        print("Press 1 to insert new user details (IT IS FOR BANK OFFICE PURPOSE)")
        print()
        print("Press 2 to display all the user details")
        print()
        print("Press 3 to delete a user details")
        print()
        print("Press 4 to update the user details")
        print()
        print("Press 5 to display a specific user details")
        print()
        print("Press 6 to exit from user details")
        print()
        try:
            choice=int(input())
            if choice==1:
                print("Enter acc no in 4-digits integer form\n")
                acc_no = int(input())
                print("Enter Your name in alphabet form\n")
                userName = input()
                print("Enter ifsc no in alphabet-integer form\n")
                ifsc = input()
                print("Enter current balance in integer form\n")
                cur_bal =int(input())
                print("Enter withdral balance in integer form\n")
                withdral_bal = int(input())
                print("Enter remaining balance in integer form\n")
                remaining_bal = int(input())
                print()
                print()
                db.insert_data(acc_no,userName,ifsc,cur_bal,withdral_bal,remaining_bal)
                print()
                print()
            elif choice==2:
                db.fetch_all()
                print()
                print()
            elif choice==3:
                print("Enter acc no in 4-digits integer form\n")
                acc_no = int(input())
                print()
                print()
                db.delete_user(acc_no)
                print()
                print()
            elif choice==4:
                print("Enter acc no in 4-digits integer form\n")
                acc_no = int(input())
                print("Enter New User name in alphabet form\n")
                userName = input()
                print()
                print()
                db.update_user(acc_no,userName)
                print()
                print()
            elif choice==5:
                print("Enter acc no in 4-digits integer form\n")
                acc_no=int(input())
                db.fetch_spe(acc_no)
            elif choice==6:
                print()
                print("Thank You and Visit again")
                break
            else:
                print("Invalid Input! Try again")
                print()
        except Exception as e:
            print(e)
            print("Invalid Details! Try again")
if __name__ == "__main__":
    main()
    