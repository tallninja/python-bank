

class User:
    '''
    This class represents the account holder

    '''

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = str(phone)
        self.email = email

    def __repr__(self):
        return (
            "User("
            f"first_name: {self.first_name}, "
            f"last_name: {self.last_name}, "
            f"phone: {self.phone}, "
            f"email: {self.email}"
            ")"
        )


def main():
    user = User("Ernest", "Wambua", "0719286396", "ernestwambua2@gmail.com")
    print(user)


if __name__ == "__main__":
    main()
