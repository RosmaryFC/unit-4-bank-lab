from bank import Bank


class Customer(Bank):

    def __init__(self,account, first_name, last_name, password, checking=0, savings=0):
        self.__account = account
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
        self.checking = checking
        self.savings = savings

    def get_info(self):
        return[self.__account, self.__first_name, self.__last_name, self.__password, self.checking, self.savings]

    def create_checking(self):
        pass

    def create_savings(self):
        pass

    def deposit(self, account_type, amount):
        account_type = account_type
        if account_type == 's':
            self.savings += amount
            print(f"savings {self.savings}")
        elif account_type == 'c':
            self.checking += amount
            print(f"checking {self.checking}")

    def withdraw(self, account_type, amount):
        account_type = account_type
        if account_type == 's':
            self.savings -= amount
            print(f"savings {self.savings}")
        elif account_type == 'c':
            self.checking -= amount
            print(f"checking {self.checking}")


    def transfer(self, from_account, to_account):
        pass
