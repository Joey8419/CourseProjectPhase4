from datetime import datetime

# --- Employee Management ---
# Function to input and return the employee's name
def employee_name():
    name = input("Enter the employee's name (or type 'End' to exit): ")
    return name

# Function to input and return total amount of hours worked
def total_hours_worked():
    hours = float(input("Enter the total amount of hours worked: "))
    while hours < 0:
        print("Hours must be more than 0. Please try again!")
        hours = float(input("Enter the total amount of hours worked: "))
    return hours

# Function for the hourly rate
def hourly_rate():
    rate = float(input("Enter the hourly rate: $"))
    while rate < 0:
        print("Hourly rate must be more than 0. Please try again!")
        rate = float(input("Enter the hourly rate: $"))
    return rate

# Function for income tax rate
def input_tax_rate():
    tax_rate = float(input("Enter the income tax rate (as a %): "))
    while tax_rate < 0 or tax_rate > 100:
        print("Tax rate must be between 0 and 100. Please try again!")
        tax_rate = float(input("Enter the income tax rate (as a %): "))
    return tax_rate / 100

# Function for 'from' and 'to' dates
def input_dates():
    from_date = input("Enter the 'From' date (mm/dd/yyyy): ")
    to_date = input("Enter the 'To' date (mm/dd/yyyy): ")
    return from_date, to_date

# Function to calculate gross pay, income tax, and net pay
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Function to display employee details
def employee_details(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print(f"\nEmployee: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: ${rate}")
    print(f"Gross Pay: ${gross_pay}")
    print(f"Income Tax Rate: {tax_rate}")
    print(f"Income Taxes: ${income_tax}")
    print(f"Net Pay: ${net_pay}\n")

# Function to display the total summary for all employees
def employee_total(summary):
    print(f"\nTotal Summary:")
    print(f"Total Employees: {summary['total_employees']}")
    print(f"Total Hours Worked: {summary['total_hours']}")
    print(f"Total Gross Pay: ${summary['total_gross_pay']}")
    print(f"Total Income Taxes: ${summary['total_income_tax']}")
    print(f"Total Net Pay: ${summary['total_net_pay']}\n")

# Function to write employee data to a file
def write_employee_to_file(employee_data):
    with open("employee_data.txt", "a") as file:
        file.write("|".join(map(str, employee_data.values())) + "\n")

# Function to read employee data from a file and process it
def read_and_process_employee_data(from_date):
    summary = {"total_employees": 0, "total_hours": 0, "total_gross_pay": 0, "total_income_tax": 0, "total_net_pay": 0}
    with open("employee_data.txt", "r") as file:
        for line in file:
            fields = line.strip().split("|")
            record_from_date, to_date, name, hours, rate, tax_rate, gross_pay, income_tax, net_pay = fields
            hours = float(hours)
            rate = float(rate)
            tax_rate = float(tax_rate)
            gross_pay = float(gross_pay)
            income_tax = float(income_tax)
            net_pay = float(net_pay)
            
            if from_date == "All" or from_date == record_from_date:
                print(f"\nFrom Date: {record_from_date}, To Date: {to_date}, Employee: {name}")
                print(f"Hours Worked: {hours}")
                print(f"Hourly Rate: ${rate}")
                print(f"Gross Pay: ${gross_pay}")
                print(f"Income Tax Rate: {tax_rate}")
                print(f"Income Taxes: ${income_tax}")
                print(f"Net Pay: ${net_pay}")
                
                summary["total_employees"] += 1
                summary["total_hours"] += hours
                summary["total_gross_pay"] += gross_pay
                summary["total_income_tax"] += income_tax
                summary["total_net_pay"] += net_pay

    employee_total(summary)

# Function to collect employee data
def employee_data():
    employees = []
    while True:
        name = employee_name()
        if name.lower() == 'end':
            break
        from_date, to_date = input_dates()
        hours = total_hours_worked()
        rate = hourly_rate()
        tax_rate = input_tax_rate()
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
        
        employee_data = {'from_date': from_date, 'to_date': to_date, 'name': name, 'hours': hours, 'rate': rate, 
                         'tax_rate': tax_rate, 'gross_pay': gross_pay, 'income_tax': income_tax, 'net_pay': net_pay}
        employees.append(employee_data)
        
        write_employee_to_file(employee_data)
        employee_details(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

    from_date_input = input("Enter the 'From' date to filter data (mm/dd/yyyy) or type 'All' to display all records: ")
    while True:
        try:
            if from_date_input != "All":
                from_date_input = datetime.strptime(from_date_input, "%m/%d/%Y").strftime("%m/%d/%Y")
            break
        except ValueError:
            from_date_input = input("Invalid date format. Please enter a valid 'From' date (mm/dd/yyyy): ")

    read_and_process_employee_data(from_date_input)


# --- User Management ---
def load_user_data():
    user_data = []  
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                user_id, _, _ = line.strip().split("|")  
                user_data.append(user_id)  
    except FileNotFoundError:
        print("No user data file found. Starting fresh.")
    return user_data  

def add_new_user():
    user_data = load_user_data()  
    while True:
        user_id = input("Enter user ID (or 'End' to stop): ")
        if user_id.lower() == 'end':  
            break
        if user_id in user_data:  
            print("User ID already exists. Please choose another one.")  
            continue
        
        password = input("Enter password: ")  
        auth_code = input("Enter authorization code (Admin/User): ").capitalize()  

        if auth_code not in ["Admin", "User"]: 
            print("Invalid authorization code. Please enter 'Admin' or 'User'.")
            continue  

        with open("user_data.txt", "a") as file:
            file.write(f"{user_id}|{password}|{auth_code}\n")  
        user_data.append(user_id)  
        print(f"User {user_id} added successfully.")  

def display_all_users():
    try:
        with open("user_data.txt", "r") as file:
            print("\nUser Data:")  
            for line in file:
                user_id, password, auth_code = line.strip().split("|")  
                print(f"User ID: {user_id}, Password: {password}, Authorization: {auth_code}")
    except FileNotFoundError:
        print("No user data found.")  

class Login:
    def __init__(self, user_id, password, auth_code):
        self.user_id = user_id  
        self.password = password  
        self.auth_code = auth_code  

def user_login():
    user_data = load_user_data()  
    if not user_data:
        print("No user data found. Please create a new user.")
        add_new_user()  
        return None  

    user_id = input("Enter user ID: ")  
    if user_id not in user_data:
        print("User ID not found.")  
        return None

    password = input("Enter password: ")  

    with open("user_data.txt", "r") as file:
        for line in file:
            stored_user_id, stored_password, auth_code = line.strip().split("|")
            if stored_user_id == user_id and stored_password == password:
                login_user = Login(user_id, stored_password, auth_code)  
                return login_user  
    print("Incorrect password.")  
    return None  

def display_user_data(login_user):
    if login_user.auth_code == "Admin":  
        print("\nAdmin Access: You can add or view user data.")
        manage_admin_tasks()  
    elif login_user.auth_code == "User":  
        print("\nUser Access: You can only view user data.")
        display_all_users()  

def manage_admin_tasks():
    while True:
        print("\nAdmin Menu:")
        print("1. Add New User")
        print("2. Display All Users")
        print("3. Enter Employee Data")
        print("4. Log Out")
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_user()  
        elif choice == "2":
            display_all_users()
        elif choice == "3":
            employee_data()  
        elif choice == "4":
            print("Logging out...")  
            break  
        else:
            print("Invalid choice. Try again.")  

def main():
    while True:
        login_user = user_login()  
        if login_user is None:
            break  
        display_user_data(login_user)  

if __name__ == "__main__":
    main()  