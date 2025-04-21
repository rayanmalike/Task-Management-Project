from project import Project

class ProjectManager:
    _instance = None

    def _init_(self):
        if ProjectManager._instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            ProjectManager._instance = self
            self.tasks = {}
    
    @staticmethod
    def get_instance():
        if ProjectManager._instance is None:
            ProjectManager()
        return ProjectManager._instance

    def create_project():
        #create project and add to database
        pass

    def update_project():
        #update project in database
        pass

    def delete_project():
        #remove project in database
        pass

    def _save_project_to_file():
        pass