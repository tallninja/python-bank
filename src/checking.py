import os
import json
from account import Account

DATABASE_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "database")

try:
    with open(os.path.join(DATABASE_PATH, "checking.json"), "r") as checking_data_base:
        ACCOUNTS = json.load(checking_data_base)
    # print(accounts)
except Exception as e:
    ACCOUNTS = []


class Checking(Account):
    '''
    Represents a checking account
     1. Deposit funds
     2. Withdraw funds
     3. Check balance
    '''

    def __init__(self) -> None:
        super().__init__()
        self.balance = float(0)

    def parse_accounts(self, account):
        return f"{account.get('id')}. [Name: {account.get('first_name')}, Balance: {account.get('balance')}, Status: {account.get('status')}]"

    def create_account(self):
        self.status = "OPEN"
        ACCOUNTS.append(self.to_json())

    def save_account(self):
        data = json.dumps(ACCOUNTS, indent=4)
        file = os.path.join(DATABASE_PATH, "checking.json")
        with open(file, "w") as checking_data_base:
            checking_data_base.write(data)

    def deposit_funds(self):
        '''
        Deposit funds to our account
        '''
        for account in ACCOUNTS:
            print(self.parse_accounts(account))

        id = int(input("Enter Account ID: >>> "))

        for account in ACCOUNTS:
            if account.get("id") == id:
                if account.get("status") == "OPEN":
                    amount = float(
                        input("Enter the amount you want to deposit: >>> "))
                    float(amount)
                    account['balance'] += amount
                    self.save_account()
                    print("Funds deposited successfully !")
                    self.start()
                else:
                    raise Exception("Account is closed !")
            else:
                pass

    def withdraw_funds(self) -> None:
        '''
        Withdraw funds from our account
        '''

        for account in ACCOUNTS:
            print(self.parse_accounts(account))

        id = int(input("Enter Account ID: >>> "))

        for account in ACCOUNTS:
            if account.get("id") == id:
                if account.get("status") == "OPEN":
                    amount = float(
                        input("Enter the amount you want to withdraw: >>> "))
                    float(amount)
                    if account["balance"] - amount >= 0:
                        account['balance'] -= amount
                        self.save_account()
                        print(f"Successfully withdrawed {amount}!")
                        self.start()
                    else:
                        raise Exception("Insufficient Funds !")
                else:
                    raise Exception("Account is closed !")
            else:
                pass

    def close_account(self):
        for account in ACCOUNTS:
            print(self.parse_accounts(account))

        id = int(input("Enter Account ID: >>> "))

        for account in ACCOUNTS:
            if account.get("id") == id:
                if account.get("status") == "OPEN":
                    account["status"] = "CLOSED"
                    self.save_account()
                    print("Successfully closed the account !")
                    self.start()
                else:
                    raise Exception("The account is already closed !")
            else:
                pass

    def to_json(self):
        '''Serializes account object type to json format'''
        if self.status == "OPEN":
            return self.__dict__
        else:
            raise Exception("Account does not exist !")

    def __repr__(self) -> str:
        return (
            "Checking("
            f"balance: {self.balance}"
            ")"
        )


def main():
    account = Checking()
    account.start()


if __name__ == "__main__":
    main()
