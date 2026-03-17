class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")
        print("-" * 40)


def process_managers():
    managers = []

    for i in range(10):
        print(f"\nEnter details for Manager {i+1}")
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        department = input("Department: ")

        manager = Manager(name, age, salary, department)
        managers.append(manager)

    print("\n--- Manager Details ---")
    for m in managers:
        m.display()

process_managers()