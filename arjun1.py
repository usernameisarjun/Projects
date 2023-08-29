class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def search_by_age(self, age):
        result = []
        for employee in self.employees:
            if employee.age == age:
                result.append(employee)
        return result

    def search_by_name(self, name):
        result = []
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                result.append(employee)
        return result

    def search_by_salary(self, operator, value):
        result = []
        for employee in self.employees:
            if operator == '>' and employee.salary > value:
                result.append(employee)
            elif operator == '<' and employee.salary < value:
                result.append(employee)
            elif operator == '>=' and employee.salary >= value:
                result.append(employee)
            elif operator == '<=' and employee.salary <= value:
                result.append(employee)
        return result

def main():
    emp_table = EmployeeTable()

    emp_table.add_employee("161E90", "Raman", 41, 56000)
    emp_table.add_employee("161F91", "Himadri", 38, 67500)
    emp_table.add_employee("161F99", "Jaya", 51, 82100)
    emp_table.add_employee("171E20", "Tejas", 30, 55000)
    emp_table.add_employee("171G30", "Ajay", 45, 44000)

    print("Search options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        result = emp_table.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = emp_table.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (> / < / <= / >=): ")
        value = int(input("Enter value: "))
        result = emp_table.search_by_salary(operator, value)
    else:
        print("Invalid choice")
        return

    if result:
        print("Search results:")
        for employee in result:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
#arjun
