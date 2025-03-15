import mysql.connector as mc
connection = mc.connect(host = 'localhost',
                        database = 'gas_booking_system',
                        user = 'root',
                        password = 'root')
c = connection.cursor()

#welcome screen
def welcome():
    print('=============================\nWelcome to Gas Booking System\n=============================')
    print('1. Register\n2. Login')
    rorl = int(input("Select option:"))
    if rorl == 1:
        register()
    elif rorl == 2:
        login()

#for existing users
def login():
    print('-----------------------------\nLogin\n-----------------------------')
    username = input("Enter your Username:")
    password = input("Enter your Password:")
    c.execute(f"SELECT * FROM users WHERE UserName = '{username}' AND Password = '{password}'")
    a = c.fetchone()
    if a:
        role = a[-1]
        if role == 'admin':
            admin_menu()
        elif role == 'employee':
            employee_menu()
        elif role == 'customer':
            customer_menu(a[0])
    else:
        print("No user with given credentials")

#for new customers
def register():
    print('-----------------------------\nRegister\n-----------------------------')
    while True:
        username = input("Enter your Username:")
        c.execute(f"SELECT * FROM users WHERE UserName = '{username}'")
        a = c.fetchone()
        if a:
            print("Username is already in use, please select a different username")
        else:
            print("Username is available")
            password = input("Enter your Password:")
            c.execute("INSERT INTO users (username, password, role) VALUES ('{}','{}','{}')".format(username,password,'customer'))
            custname = input("Enter your name:")
            custaddress = input("Enter your address:")
            custemail = input("Enter your Email:")
            custphone = input("Enter your phone number:")
            c.execute("INSERT INTO customers (UserName, CustName, CustAddress, CustEmail, CustPhone) VALUES ('{}','{}','{}','{}','{}')"
                .format(username, custname, custaddress, custemail, custphone))
            connection.commit()
            print("User registered successfully")
            welcome()

def admin_menu():
    print('-----------------------------\nAdmin Menu\n-----------------------------')
    print('1. Manage Customers\n2. Manage Employees\n3. Manage Orders\n4. Exit')
    admin_choice = int(input("Select option:"))
    if admin_choice == 1:
        manage_cust()
    elif admin_choice == 2:
        manage_emp()
    elif admin_choice == 3:
        manage_order()
    elif admin_choice == 4:
        exit()

def manage_cust():
    while True:
        print('-----------------------------\nManage Customers\n-----------------------------')
        print('1. View all Customers\n2. Search Customers\n3. Add Customer\n4. Update Customer\n5. Delete Customer\n6. Back')
        choice = int(input("Select option:"))
        if choice == 1:
            c.execute("SELECT * FROM customers")
            a = c.fetchall()
            if a:
                print(a)
            else:
                print("No customers")
        elif choice == 2:
            search = input("Enter Username to Search:")
            c.execute(f"SELECT * FROM customers WHERE UserName = '{search}'")
            a = c.fetchall()
            if a:
                print(a)
            else:
                print("Username not found")
        elif choice == 3:
            register()
        elif choice == 4:
            update = input("Enter Username to update:")
            c.execute(f"SELECT * FROM customers WHERE UserName = '{update}'")
            a = c.fetchone()
            if a:
                newname = input("Enter name:")
                newaddress = input("Enter address:")
                newemail = input("Enter Email:")
                newphone = input("Enter phone number:")
                c.execute(f"UPDATE customers SET CustName = '{newname}',CustAddress = '{newaddress}',CustEmail = '{newemail}',CustPhone = '{newphone}'")
                connection.commit()
                print("Customer details updated")
            else:
                print("Username not found")
        elif choice == 5:
            erase = input("Enter UserName of user to be deleted:")
            c.execute(f"DELETE FROM customers WHERE UserName = '{erase}'")
            connection.commit()
            print("User deleted")
        elif choice == 6:
            admin_menu()

def manage_emp():
    while True:
        print('-----------------------------\nManage Employees\n-----------------------------')
        print('1. View all Employees\n2. Search Employee\n3. Add Employee\n4. Update Employee\n5. Delete Employee\n6. Back')
        choice = int(input("Select option:"))
        if choice == 1:
            c.execute("SELECT * FROM employees")
            a = c.fetchall()
            if a:
                print(a)
            else:
                print("No employees")
        elif choice == 2:
            search = input("Enter Username to Search:")
            c.execute(f"SELECT * FROM employees WHERE UserName = '{search}'")
            a = c.fetchall()
            if a:
                print(a)
            else:
                print("Username not found")
        elif choice == 3:
            while True:
                username = input("Enter your Username:")
                c.execute(f"SELECT * FROM users WHERE UserName = '{username}'")
                a = c.fetchone()
                if a:
                    print("Username is already in use, please select a different username")
                else:
                    print("Username is available")
                    password = input("Enter your Password:")
                    c.execute("INSERT INTO users (username, password, role) VALUES ('{}','{}','{}')".format(username, password,'employee'))
                    empname = input("Enter employee's name:")
                    salary = int(input("Enter employee's salary:"))
                    empemail = input("Enter employee's Email:")
                    empphone = input("Enter employee's phone number:")
                    c.execute("INSERT INTO employees (UserName, EmpName, EmpSalary, EmpEmail, EmpPhone) VALUES ('{}','{}',{},'{}','{}')"
                        .format(username, empname, salary, empemail, empphone))
                    connection.commit()
                    print("Employee registered successfully")
                    break
        elif choice == 4:
            update = input("Enter Username to update:")
            c.execute(f"SELECT * FROM employees WHERE UserName = '{update}'")
            a = c.fetchone()
            if a:
                newname = input("Enter new name:")
                newsalary = int(input("Enter new salary:"))
                newemail = input("Enter new Email:")
                newphone = input("Enter new phone number:")
                c.execute(f"UPDATE employees SET EmpName = '{newname}',EmpSalary = '{newsalary}',EmpEmail = '{newemail}',EmpPhone = '{newphone}'")
                connection.commit()
                print("Employee details updated")
            else:
                print("Username not found")
        elif choice == 5:
            erase = input("Enter UserName of user to be deleted:")
            c.execute(f"DELETE FROM customers WHERE UserName = '{erase}'")
            connection.commit()
            print("User deleted")
        elif choice == 6:
            admin_menu()

def manage_order():
    while True:
        print('-----------------------------\nManage Orders\n-----------------------------')
        print('1. View all Orders\n2. Search Order\n3. Add Order\n4. Update Order\n5. Delete Order\n6. Change default price\n7. Back')
        choice = int(input("Select option:"))
        if choice == 1:
            c.execute("SELECT * FROM orders")
            a = c.fetchall()
            if a:
                print(a)
            else:
                print("No orders")
        elif choice == 2:
            search = input("Enter OrderID to Search:")
            c.execute(f"SELECT * FROM orders WHERE OrderID = '{search}'")
            a = c.fetchall()
            if a:
                print(a)
            else:
                print("Order ID not found")
        elif choice == 3:
            username = input("Enter the Username of the customer:")
            c.execute(f"SELECT * FROM customers WHERE UserName = '{username}'")
            customer = c.fetchone()
            if not customer:
                print("Customer with Username does not exist")
                continue
            custname = input("Enter Name of the customer:")
            address = input("Enter delivery address:")
            booking_date = input("Enter booking date (DD/MM/YYYY):")
            delivery_date = input("Enter delivery date (DD/MM/YYYY):")
            new_price = input("Enter the price of the order:")
            status = input("Enter the order status Pending or Completed:")
            c.execute(f'''INSERT INTO orders (UserName, CustName, Address, BookingDate, DeliveryDate, Price, OrderStatus)
                VALUES ('{username}','{custname}','{address}','{booking_date}','{delivery_date}',{new_price},'{status}')''')
            connection.commit()
            print("Order added successfully")
        elif choice == 4:
            update = input("Enter Order ID to update:")
            c.execute(f"SELECT * FROM orders WHERE OrderID = '{update}'")
            a = c.fetchone()
            if a:
                newname = input("Enter new name:")
                newaddress = input("Enter new address:")
                newbooking_date = input("Enter new booking date (DD/MM/YYYY):")
                newdelivery_date = input("Enter new delivery date (DD/MM/YYYY):")
                newprice = int(input("Enter new price:"))
                newstatus = input("Enter new order status Pending or Completed:")
                c.execute(f"UPDATE orders SET CustName = '{newname}',Address = '{newaddress}',BookingDate = '{newbooking_date}', DeliveryDate = '{newdelivery_date}',Price = {newprice},OrderStatus = '{newstatus}'")
                connection.commit()
                print("Order details updated")
            else:
                print("Username not found")
        elif choice == 5:
            erase = input("Enter Order ID of order to be deleted:")
            c.execute(f"DELETE FROM orders WHERE OrderID = '{erase}'")
            connection.commit()
            print("Order deleted")
        elif choice == 6:
            new_price = int(input("Enter new default price:"))
            c.execute(f"ALTER TABLE orders ALTER COLUMN Price SET DEFAULT {new_price};")
            connection.commit()
            print("Default price has been updated")
        elif choice == 7:
            admin_menu()


def employee_menu():
    while True:
        print('-----------------------------\nEmployee Menu\n-----------------------------')
        print('1. View Order Details\n2. Update Order Status\n3. Exit')
        emp_choice = int(input("Select option:"))
        if emp_choice == 1:
            orderid = int(input("Enter Order ID to search:"))
            c.execute(f"SELECT * FROM orders WHERE OrderID = {orderid}")
            a = c.fetchone()
            if a:
                print(a)
            else:
                print("No order found with the given ID")
        elif emp_choice == 2:
            orderid = int(input("Enter Order ID to search:"))
            c.execute(f"SELECT * FROM orders WHERE OrderID = {orderid}")
            a = c.fetchone()
            if not a:
                print("No order with the ID given")
                continue
            newdelivery_date = input("Enter delivery date (DD/MM/YYYY):")
            new_status = input("Enter new status Pending/Completed:")
            c.execute(f"UPDATE orders SET DeliveryDate = '{newdelivery_date}', OrderStatus = '{new_status}'")
            connection.commit()
            print("Order updated successfully")
        elif emp_choice == 3:
            exit()


def customer_menu(username):
    while True:
        print('-----------------------------\nCustomer Menu\n-----------------------------')
        print('1. Book Gas\n2. View Order Status\n3. Exit')
        cust_choice = int(input("Select option:"))
        if cust_choice == 1:
            c.execute(f"SELECT * FROM customers WHERE UserName = '{username}'")
            a = c.fetchone()
            custname = a[1]
            address = a[2]
            booking_date = input("Enter date of booking (DD/MM/YYYY):")
            orderstatus = "Pending"
            delivery_date = 'NULL'
            c.execute(f'''INSERT INTO orders (UserName, CustName, Address, BookingDate, DeliveryDate, OrderStatus)
                VALUES ('{username}','{custname}','{address}','{booking_date}','{delivery_date}','{orderstatus}')''')
            connection.commit()
            print("Gas booked successfully")
        elif cust_choice == 2:
            c.execute(f"SELECT * FROM orders WHERE UserName = '{username}'")
            a = c.fetchall()
            print(a)
        elif cust_choice == 3:
            exit()

welcome()