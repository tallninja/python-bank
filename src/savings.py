import os
import json
from account import Account

DATABASE_PATH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "database")

try:
    with open(os.path.join(DATABASE_PATH, "savings.json"), "r") as checking_data_base:
        ACCOUNTS = json.load(checking_data_base)
    # print(accounts)
except Exception as e:
    ACCOUNTS = []


class Savings(Account):
    '''
    Represents a savings account
       1. Limit to the number of withdrawals over a given interval
       2. Minimum balance requirements
       3. Interest rates - the saved funds earn interest over time ***
    '''

    def __init__(self):
        super().__init__()
        self.balance = float(0)
        self.minimum_balance = float(100)
        self.max_num_of_withdrawals = 3

    def parse_accounts(self, account):
        return f"{account.get('id')}. [Name: {account.get('first_name')}, Balance: {account.get('balance')}, Status: {account.get('status')}]"

    def create_account(self):
        self.status = "OPEN"
        ACCOUNTS.append(self.to_json())

    def save_account(self):
        data = json.dumps(ACCOUNTS, indent=4)
        file = os.path.join(DATABASE_PATH, "savings.json")
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
                    if amount >= account["minimum_balance"]:
                        account["balance"] += amount
                        self.save_account()
                    else:
                        raise Exception(
                            f"Cannot deposit funds less than {account['minimum_balance']} !")
                else:
                    raise Exception("Account is closed !")
            else:
                pass

    def withdraw_funds(self):
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
                    if self.max_num_of_withdrawals > 0:
                        if account["balance"] - amount >= self.minimum_balance:
                            account["balance"] -= amount
                            account["max_num_of_withdrawals"] -= 1
                            self.save_account()
                        else:
                            raise Exception("Insufficient funds !")
                    else:
                        raise Exception(
                            "You have exhausted your withdrawal tries !")
                else:
                    raise Exception("Account does not exist !")
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
                else:
                    raise Exception("The account is already closed !")
            else:
                pass

    def to_json(self) -> dict:
        '''Serializes account object type to json format'''
        if self.status == "OPEN":
            return self.__dict__
        else:
            raise Exception("Account does not exist !")

    def __repr__(self) -> str:
        return (
            "Savings("
            f"balance: {self.balance}, "
            f"minimum_balance: {self.minimum_balance}, "
            f"max_num_of_withdrawals: {self.max_num_of_withdrawals}"
            ")"
        )


def main():
    account = Savings()
    account.start()


if __name__ == "__main__":
    main()
