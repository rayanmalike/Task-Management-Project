from user import User
class Manager(User):
    def __init__(self, id, name, email, password,  role):
        super().__init__(id, name, email, password, role)
        self.tasks = {}
        self.projects = {}
