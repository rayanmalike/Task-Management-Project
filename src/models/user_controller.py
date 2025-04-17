from manager import Manager
from employee import Employee
import csv
from typing import List, Optional

class UserController:
    _instance = None
    
    def __init__(self):
        if UserController._instance is not None:
            raise Exception("This class is a singleton!")
        UserController._instance = self
        self.employees = {}
        self.managers = {}
        
    @staticmethod
    def get_instance():
        if UserController._instance is None:
            UserController()
        return UserController._instance
    
    def create_employee(self, id: int, name: str, email: str, password: str) -> Employee:
        employee = Employee(id, name, email, password, "employee")
        self.employees[id] = employee
        self._save_employees_to_csv()
        return employee
    
    def create_manager(self, id: int, name: str, email: str, password: str) -> Manager:
        manager = Manager(id, name, email, password, "manager")
        self.managers[id] = manager
        self._save_managers_to_csv()
        return manager
    
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        return self.employees.get(employee_id)
    
    def get_manager(self, manager_id: int) -> Optional[Manager]:
        return self.managers.get(manager_id)
    
    def get_all_employees(self) -> List[Employee]:
        return list(self.employees.values())
    
    def get_all_managers(self) -> List[Manager]:
        return list(self.managers.values())
    
    def _save_employees_to_csv(self):
        with open("employees.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Password", "Role"])
            for employee in self.employees.values():
                writer.writerow([
                    employee.get_user_id(),
                    employee.get_username(),
                    employee.get_email(),
                    employee.get_password(),
                    employee.get_role()
                ])
    
    def _save_managers_to_csv(self):
        with open("managers.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Password", "Role"])
            for manager in self.managers.values():
                writer.writerow([
                    manager.get_user_id(),
                    manager.get_username(),
                    manager.get_email(),
                    manager.get_password(),
                    manager.get_role()
                ])
    
    def _load_from_csv(self):
        try:
            # Load employees
            with open("employees.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    id = int(row["ID"])
                    self.employees[id] = Employee(
                        id,
                        row["Name"],
                        row["Email"],
                        row["Password"],
                        row["Role"]
                    )
            
            # Load managers
            with open("managers.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    id = int(row["ID"])
                    self.managers[id] = Manager(
                        id,
                        row["Name"],
                        row["Email"],
                        row["Password"],
                        row["Role"]
                    )
        except FileNotFoundError:
            print("One or both CSV files not found. Starting with empty collections.")

# # Example usage:
# uc = UserController.get_instance()

# # Create some users
# emp1 = uc.create_employee(1, "John Doe", "john@example.com", "pass123")
# emp2 = uc.create_employee(2, "Jane Smith", "jane@example.com", "pass456")
# mgr1 = uc.create_manager(3, "Alice Johnson", "alice@example.com", "pass789")

# # Load existing users from CSV
# uc._load_from_csv()

# # Get all employees and managers
# all_employees = uc.get_all_employees()
# all_managers = uc.get_all_managers()


