from lib.dbManager import Db_manager




exit = False
while not exit:
    print("========= DB Manager =============")
    print("""
    1. Add user
    2. Login to the database
    3. Show users
    4. Delete user
    0. Exit
    """)
    choice = int(input())
    if choice == 1:
        try:
            one = Db_manager("localhost", "root", "", "loginsystem")
            one.add_user()
        except:
            print("This email already exists. Enter another email")
            
       
    elif choice == 2:
        try:
            two = Db_manager("localhost", "root", "", "loginsystem")
            par = two.check_user()
            password = input('Enter password: ')
            if par == (password,):
                print("Welcom user")
            else:
                print("Invalid password")
        except:
            print("Invalid email")

        
    elif choice == 3:
        try:
            three = Db_manager("localhost", "root", "", "loginsystem")
            res = three.show_all_users()
            for item in res:
                print(item)
        except:
            print("Error db")
    elif choice == 4:
        try:
            four = Db_manager("localhost", "root", "", "loginsystem")
            res = four.show_all_users()
            for item in res:
                print(item)
            four.del_user()  
        except:
            ("Enter corect ID")   
    elif choice == 0:
        exit = True
    else:
        print("read manual")