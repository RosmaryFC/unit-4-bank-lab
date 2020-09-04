from customer import Customer


class Bank:

    def __init__(self, name):
        self.name = name
        self.customers = {}

    def seed_customers(self, data):
        for row in data.items():
            new_customer = Customer(row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4])
            print(new_customer.get_info())
            self.customers[row[0]] = new_customer

    # # def add_customer(self, first_name, last_name,):
    # #     customer = Customer(first_name, last_name)
    # #     pass
    #
    # def get_customer(self):
    #     pass
    #
    # def set_customer(self):
    #     pass

    # def require_login(self, first_name, last_name, password):
    #
    #     if self.__password == password:
    #         return customer
    #     else
    #         return "invalid password"
