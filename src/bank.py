import os
import sys
# from account import Account

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Bank:
    def __init__(self, name):
        self.name = name
        self.start_option = None

    def start(self):
        os.chdir(BASE_PATH)
        try:
            os.listdir().index("database")
        except:
            os.mkdir("database")

        print(f'''
            Welcome To {self.name} Bank :)

            What would you like us to do for you ?

                1. Open an account.
                2. Close an account.
                3. withdraw funds.
                4. Deposit funds.
                0. Quit

        ''')
        self.start_option = int(input(">>> "))
        self.handle_start_options()

    def handle_start_options(self):
        if self.start_option == 1:
            self.open_account()
            pass
        elif self.start_option == 2:
            self.close_account()
            pass
        elif self.start_option == 3:
            self.withdraw_funds()
            pass
        elif self.start_option == 4:
            self.deposit_funds()
            pass
        elif self.start_option == 0:
            self.close()
        else:
            print(f"{self.start_option} is not a valid choice !")
            self.start()

    def open_account(self):
        pass

    def close_account(self):
        pass

    def withdraw_funds(self):
        pass

    def deposit_funds(self):
        pass

    def close(self):
        sys.exit("Good Bye !")


def main():
    bank = Bank("Money")
    bank.start()


if __name__ == "__main__":
    main()
