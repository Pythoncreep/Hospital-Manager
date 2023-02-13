print(".................Welcome to Hospital Manager................")

# Admin Login
#admin username : admin
#password : password
def admin_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Add Department
departments = []
def add_department():
    department_name = input("Enter department name: ")
    department_image = input("Enter department profile image: ")
    year_founded = input("Enter year founded: ")
    description_dep = input("Enter description")
    departments.append({
        "department_name": department_name,
        "department_image": department_image,
        "year_founded": year_founded,
        "description_dep": description_dep
    })

# Edit Department
def edit_department():
    department_name = input("Enter department name: ")
    for department in departments:
        if department["department_name"] == department_name:
            department["name"] = input("Enter new department name: ")
            department["image"] = input("Enter new department profile image: ")
            department["year_founded"] = input("Enter new year founded: ")
            break
    else:
        print("Department not found.")

# Delete Department
def delete_department():
    department_name = input("Enter department name: ")
    for index, department in enumerate(departments):
        if department["name"] == department_name:
            del departments[index]
            break
    else:
        print("Department not found.")


# Add Department Head
departmentheads = []
def add_department_head():
    head_name = input("Enter head name: ")
    employee_number = input("Enter employee number: ")
    head_age= int(input("Enter age: "))
    head_profile_image = input("Enter profile image: ")
    head_profile_description = input("Enter profile description: ")
    departmentheads.append({
        "head_name": head_name,
        "employee_number": employee_number,
        "age": head_age,
        "image": head_profile_image,
        "description": head_profile_description,
        "department": department["name"]
    })

# Edit Department Head
def edit_department_head():
    head_name = input("Enter head name: ")
    for head in departmentheads:
        if head["head_name"] == head_name:
            head["name"] = input("Enter new head name: ")
            head["employee_number"] = input("Enter new employee number: ")
            head["age"] = int(input("Enter new age: "))
            head["image"] = input("Enter new profile image: ")
            head["description"] = input("Enter new profile description: ")
            break
    else:
        print("Department head not found.")

# Delete Department Head
def delete_department_head():
    head_name = input("Enter head name: ")
    for index, head in enumerate(departmentheads):
        if head["name"] == head_name:
            del departmentheads[index]
            break
    else:
        print("Department head not found.")

# Add Employee
employees = []
def add_employee():
    employee_name = input("Enter name: ")
    employee_number = input("Enter employee number: ")
    employee_age = int(input("Enter age: "))
    profile_image = input("Enter profile image: ")
    profile_description = input("Enter profile description: ")
    department = choose_department()
    report_to = choose_department_head(department)
    employees.append({
        "name": employee_name,
        "employee_number": employee_number,
        "age": employee_age,
        "image": profile_image,
        "description": profile_description,
        "department": department["name"],
        "report_to": report_to["name"]
    })

# Edit Employee
def edit_employee():
    name = input("Enter name: ")
    for employee in employees:
        if employee["name"] == name:
            employee["name"] = input("Enter new name: ")
            employee["employee_number"] = input("Enter new employee number: ")
            employee["age"] = int(input("Enter new age: "))
            employee["image"] = input("Enter new profile image: ")
            employee["description"] = input("Enter new profile description: ")
            employee["department"] = department_name()["name"]
            employee["report_to"] = head_name(employee["department"])["name"]
            break
    else:
        print("Employee not found.")

# Delete Employee
def delete_employee():
    name = input("Enter name: ")
    for index, employee in enumerate(employees):
        if employee["name"] == employee_name:
            del employees[index]
            break
    else:
        print("Employee not found.")

# Main program
employees = []
if admin_login():
    while True:
        print("1. Add Department")
        print("2. Edit Department")
        print("3. Delete Department")
        print("4. Add Department Head")
        print("5. Edit Department Head")
        print("6. Delete Department Head")
        print("7. Add Employee")
        print("8. Edit Employee")
        print("9. Delete Employee")
        print("10. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            add_department()
        elif choice == "2":
            edit_department()
        elif choice == "3":
            delete_department()
        elif choice == "4":
            add_department_head()
        elif choice == "5":
            edit_department_head()
        elif choice == "6":
            delete_department_head()
        elif choice == "7":
            add_employee()
        elif choice == "8":
            edit_employee()
        elif choice == "9":
            delete_employee()
        elif choice == "10":
            break
        else:
            print("Invalid choice.")



        
    
       
        
