from user import User

class Employee(User):
    def __init__(self, id, name, email, password, role):
        super().__init__(id, name, email,password, role)
        self.assigned_tasks = []

    def get_task(self, input):
        if input <= 0 or input > (len(self.assigned_tasks) - 1) :
            raise ValueError('Not a valid input.')
        elif 1 <= input <=  (len(self.assigned_tasks) - 1) :
            return self.assigned_tasks[input]

    def get_task_description(self, task):
        return task.get_description()

    #Removed submit_task, handled by task_controller object

    def get_task_due_date(self, task):
        return task.get_due_date()

    def get_task_priority(self, task):
        return task.get_priority()

    def get_project_description(self, project):
        return project.get_description()

    def get_project_end_date(self, project):
        return project.get_end_date()


    