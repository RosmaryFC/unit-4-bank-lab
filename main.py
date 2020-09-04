from customer import Customer


def read_csv(file_name):
    # we are creating an empty dict to hold the data
    # from the csv file
    data = {}
    record_counter = 0
    """
   this function will read all the data from the local csv file
   and convert it to a dict data type and return the values
   """
    try:
        # we are going to read the file, and it will be
        # in read ony mode
        file = open(file_name, 'r')
        # print(type(file))
        # we are reading one line at a time from the file object
        for line in file:
            # print(type(line))
            # we are split each row in our file by using the ,
            # column is a List data type
            column = line.split(',')
            data[column[0].rstrip('\n')] = [column[1], column[2], column[3], float(column[4]), float(column[5])]
            record_counter += 1
        # I'm killing the object for closing the conncetion to the file
        # this is good for security reasons
        print(f"there are {record_counter} rows in this file")
        file.close()
        return data
    except IOError:
        print("Cannot open the file")


all_data = read_csv("bank.csv")
print(all_data)

cust_1 = all_data['10001']
print(cust_1)

customer_suresh = Customer('10001', cust_1[0], cust_1[1], cust_1[2], cust_1[3], cust_1[4])
# customer_suresh = Customer(cust_1, cust_1, cust_1, cust_1)

print(customer_suresh.get_info())

