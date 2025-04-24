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
        try:
            employee = Employee(id, name, email, password, "employee")
            self.employees[id] = employee
            self._save_employees_to_csv()
            print(f"Created employee {name} successfully.")
            return employee
        except Exception as e:
            print(f"Failed to create new employee: {str(e)}")
            return None
    
    def create_manager(self, id: int, name: str, email: str, password: str) -> Manager:
        try:
            manager = Manager(id, name, email, password, "manager")
            self.managers[id] = manager
            self._save_managers_to_csv()
            print(f"Created manager {name} successfully.")
            return manager
        except Exception as e :
            print(f"Failed to create new manager: {str(e)}")
            return None
        
    def update_password(self, user_id: int, new_password: str, is_manager: bool = False) -> bool:
        try:
            if is_manager:
                if user_id in self.managers:
                    self.managers[user_id].set_password(new_password)
                    self._save_managers_to_csv()
                    print(f"Successfully updated manager password (ID: {user_id})")
                    return True
            else:
                if user_id in self.employees:
                    self.employees[user_id].set_password(new_password)
                    self._save_employees_to_csv()
                    print(f"Successfully updated employee password (ID: {user_id})")
                    return True
            return False
        except Exception as e:
            print(f"Failed to update password: {str(e)}")
            return False
        
    def update_employee_info(self, employee_id: int, new_name: str = None, new_email: str = None) -> bool:
        try:
            if employee_id in self.employees:
                employee = self.employees[employee_id]
                if new_name:
                    employee.set_name(new_name)
                if new_email:
                    employee.set_email(new_email)
                self._save_employees_to_csv()
                print(f"Successfully updated employee info (ID: {employee_id})")
                return True
            return False
        except Exception as e:
            print(f"Failed to update employee info: {str(e)}")
            return False

    def update_manager_info(self, manager_id: int, new_name: str = None, new_email: str = None) -> bool:
        try:
            if manager_id in self.managers:
                manager = self.managers[manager_id]
                if new_name:
                    manager.set_name(new_name)
                if new_email:
                    manager.set_email(new_email)
                self._save_managers_to_csv()
                print(f"Successfully updated manager info (ID: {manager_id})")
                return True
            return False
        except Exception as e:
            print(f"Failed to update manager info: {str(e)}")
            return False
        
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


