from manager import Manager
from employee import Employee
import csv
from typing import List, Optional
from user_manager_dict import UserManager


class UserController:
    """
    UserController manages employees and managers,
    handling creation, retrieval, updating, deletion, and
    saving/loading users from CSV files. Singleton pattern enforced.
    """
    _instance = None

    def __init__(self):
        """
        Initializes the UserController instance.
        Loads employees and managers from CSV files.
        """
        if UserController._instance is not None:
            raise Exception("This class is a singleton!")
        UserController._instance = self
        self.employees = {}
        self.managers = {}
        self._load_from_csv()

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of UserController.

        Returns:
            UserController: The singleton UserController instance.
        """
        if UserController._instance is None:
            UserController()
        return UserController._instance

    def create_employee(self, id: int, name: str, email: str, password: str) -> Employee:
        """
        Creates a new Employee and saves it to CSV.

        Args:
            id (int): Employee ID.
            name (str): Employee name.
            email (str): Employee email.
            password (str): Employee password.

        Returns:
            Employee: The created Employee object, or None on failure.
        """
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
        """
        Creates a new Manager and saves it to CSV.

        Args:
            id (int): Manager ID.
            name (str): Manager name.
            email (str): Manager email.
            password (str): Manager password.

        Returns:
            Manager: The created Manager object, or None on failure.
        """
        try:
            manager = Manager(id, name, email, password, "manager")
            self.managers[id] = manager
            self._save_managers_to_csv()
            print(f"Created manager {name} successfully.")
            return manager
        except Exception as e:
            print(f"Failed to create new manager: {str(e)}")
            return None

    def update_password(self, user_id: int, new_password: str, is_manager: bool = False) -> bool:
        """
        Updates the password for an employee or manager.

        Args:
            user_id (int): User ID.
            new_password (str): New password to set.
            is_manager (bool, optional): Whether the user is a manager. Defaults to False.

        Returns:
            bool: True if update was successful, False otherwise.
        """
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
        """
        Updates an employee's name and/or email address.

        Args:
            employee_id (int): Employee ID.
            new_name (str, optional): New name.
            new_email (str, optional): New email address.

        Returns:
            bool: True if update was successful, False otherwise.
        """
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
        """
        Updates a manager's name and/or email address.

        Args:
            manager_id (int): Manager ID.
            new_name (str, optional): New name.
            new_email (str, optional): New email address.

        Returns:
            bool: True if update was successful, False otherwise.
        """
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

    def get_employee(self, employee_id: int):
        """
        Retrieves an employee by ID.

        Args:
            employee_id (int): Employee ID.

        Returns:
            Employee: The employee object if found, else None.
        """
        if employee_id in self.employees:
            return self.employees.get(employee_id)

    def get_manager(self, manager_id: int):
        """
        Retrieves a manager by ID.

        Args:
            manager_id (int): Manager ID.

        Returns:
            Manager: The manager object if found, else None.
        """
        return self.managers.get(manager_id)

    def get_manager_by_username(self, username):
        """
        Retrieves a manager by username.

        Args:
            username (str): Manager username.

        Returns:
            Manager: The manager object if found, else None.
        """
        for user_id, user in self.managers.items():
            if user.get_username() == username and user.get_role().lower() == "manager":
                return user
        return None

    def get_employee_by_username(self, username):
        """
        Retrieves an employee by username.

        Args:
            username (str): Employee username.

        Returns:
            Employee: The employee object if found, else None.
        """
        for user_id, user in self.employees.items():
            if user.get_username() == username and user.get_role().lower() == "employee":
                return user
        return None

    def get_all_employees(self) -> List[Employee]:
        """
        Retrieves a list of all employees.

        Returns:
            List[Employee]: A list of Employee objects.
        """
        return list(self.employees.values())

    def get_all_managers(self) -> List[Manager]:
        """
        Retrieves a list of all managers.

        Returns:
            List[Manager]: A list of Manager objects.
        """
        return list(self.managers.values())

    def delete_employee(self, employee_id: int) -> bool:
        """
        Deletes an employee by ID and updates the CSV.

        Args:
            employee_id (int): Employee ID.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            if employee_id in self.employees:
                del self.employees[employee_id]
                self._save_employees_to_csv()
                print(f"Successfully deleted employee (ID: {employee_id})")
                return True
            print(f"Employee with ID {employee_id} not found")
            return False
        except Exception as e:
            print(f"Failed to delete employee: {str(e)}")
            print(f"Current employees: {self.employees}")
            return False

    def _save_managers_to_csv(self):
        """
        Saves all manager data to the managers.csv file.
        """
        try:
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
                print("Successfully saved managers to CSV")
        except Exception as e:
            print(f"Error saving to CSV: {str(e)}")

    def _save_employees_to_csv(self):
        """
        Saves all employee data to the employees.csv file.
        """
        try:
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
                print("Successfully saved employees to CSV")
        except Exception as e:
            print(f"Error saving to CSV: {str(e)}")

    def _load_from_csv(self):
        """
        Loads employees and managers from CSV files into memory.
        """
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
            print("Loaded Managers and Employees csv files successfully.")
        except FileNotFoundError:
            print("One or both CSV files not found. Starting with empty collections.")
        except Exception as e:
            print(str(e))

    def delete_manager(self, manager_id: int) -> bool:
        """
        Deletes a manager by ID and updates the CSV.

        Args:
            manager_id (int): Manager ID.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        try:
            if manager_id in self.managers:
                del self.managers[manager_id]
                self._save_managers_to_csv()
                print(f"Successfully deleted manager (ID: {manager_id})")
                return True
            print(f"Manager with ID {manager_id} not found")
            return False
        except Exception as e:
            print(f"Failed to delete manager: {str(e)}")
            print(f"Current managers: {self.managers}")
            return False
