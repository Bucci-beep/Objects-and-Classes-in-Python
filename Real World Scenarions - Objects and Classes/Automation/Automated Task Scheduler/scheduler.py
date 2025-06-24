# initiate the base class

class User:
    def __init__(self, name, role, tasks):
        self.name = name
        self.role = role
        # if no tasks provided, start with no tasks
        if tasks is None:
            self.tasks = []
        else:
         self.task = tasks

    def add_task(self, task):
       self.tasks.append(task)
       return f"Task '{task}' added for {self.name}."

    def view_tasks(self):
        # display all tasks in the list
        print(f"Tasks for {self.name}:")
        for task in self.tasks:
            print(f"- {task}")

class Admin(User):
    def __init__(self,name, tasks=None):
        super().__init__(name, role='admin', tasks=tasks)

    def assign_task(self, user, task):
        user.add_task(task)
        print(f"Admin {self.name} assigned task '{task}' to {user.name}")

class Developer(User):
    def __init__(self, name, tasks=None):
        super().__init__(name, role='developer', tasks=tasks)

    def push_code(self):
        print(f"{self.name} is pushing code to the repository.")

class GeneralUser(User):
    def __init__(self, name, tasks=None):
        super().__init__(name, role='general user', tasks = tasks)
