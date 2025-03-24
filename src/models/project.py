class Project:
    def __init__(self, project_id, title, description, start_date, end_date, assigned_tasks : list):
        self.id = project_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.assigned_tasks = assigned_tasks

    # Getters and setters
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_start_date(self):
        return self.start_date
      
    def get_end_date(self):
        return self.end_date

    def get_assigned_tasks(self):
        return self.assigned_tasks

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        if end_date >= self.start_date:
            raise ValueError("End date must be after Start date")
        self.end_date = end_date
