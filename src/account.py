from bank import Bank


class Account(Bank):
    '''
    This class represents a single account holder
    '''

    def __init__(self):
        super().__init__(name="Money")
        self.id = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.email = None
        self.status = "CLOSED"

    def open_account(self):
        print('''
            Please enter the following details...
        ''')
        self.id = int(input("Account ID: >>> "))
        self.first_name = str(input("First Name: >>> "))
        self.last_name = str(input("Last Name: >>> "))
        self.phone = str(input("Phone: >>> "))
        self.email = str(input("Email: >>> "))
        self.status = "OPEN"
        self.create_account()
        self.save_account()
        print("Successfully created the account !")
        self.start()

    def create_account(self):
        pass

    def save_account(self):
        pass

    def __repr__(self):
        return (
            "Account("
            f"first_name: {self.first_name}, "
            f"last_name: {self.last_name}, "
            f"phone: {self.phone}, "
            f"email: {self.email}, "
            f"status: {self.status}"
            ")"
        )


def main():
    account = Account()
    account.start()


if __name__ == "__main__":
    main()
