class Password:
    def __init__(self, app_name, user_name, password):
        self.app_name = app_name
        self.user_name = user_name
        self.password = password

    def get_app_name(self):
        return self.app_name

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.password

class Password_Manager:
    def __init__(self):
        self.list_of_passwords = []

    def store_password(self, app_name, user_name, password):
        app_data = Password(app_name, user_name, password)
        self.list_of_passwords.append(app_data)

    def get_password(self, app_name):
        current_app_data = Password(0,0,0)
        flag = False

        for app_data in self.list_of_passwords:
            if app_data.get_app_name() == app_name:
                flag = True
                current_app_data = app_data
                break

        if flag:
            print(current_app_data.get_app_name() + ":" + current_app_data.get_user_name() + ":" + current_app_data.get_password())
        else:
            print("data does not exist")

    def get_all_passsword(self):
        for app_data in self.list_of_passwords:
            print(app_data.get_app_name() + ":" + app_data.get_user_name() + ":" + app_data.get_password())

    def start_password_manager(self):
        print("welcome to the password manager application")

        while(True):
            print("Please choose an option")
            print("1.Store Password, 2.View Password, 3.View All")
            choice = int(input())

            if (choice == 1):
                print("Enter app name, user name and password")
                app_name = input()
                user_name = input()
                password = input()
                self.store_password(app_name, user_name, password)

            elif (choice == 2):
                print("Enter app name")
                app_name = input()
                self.get_password(app_name)

            elif (choice ==3):
                self.get_all_passsword()

            else:
                print("invalid choice")

            print("Do you want to continue?")
            option = input()

            if option == 'n' or option == 'N':
                break

password_manager = Password_Manager()
password_manager.start_password_manager()
