import admin
import users

def option_start() :
    user_option = int(input("Anda Sebagai?\n\n1. Admin\n2. User\n\nPilih : "))
    
    if user_option == 1 :
        admin.start()
    if user_option == 2 :
        users.order_data()

def main() :
    option_start()
    
if __name__ == '__main__' :
    main()