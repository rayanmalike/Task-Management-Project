class Permissions:
    def __init__(self, role):
        self.role = role

    def enforce_create_project(self):
        if self.role != "Manager":
            raise PermissionError("You do not have permission to create projects.")
    
    def enforce_update_project(self):
        if self.role != "Manager":
            raise PermissionError("You do not have permission to update projects.")
    
    def enforce_view_project(self):
        if self.role not in ["Manager", "Employee"]:
            raise PermissionError("You do not have permission to view projects.")
