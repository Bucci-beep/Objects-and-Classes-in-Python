from scheduler import Admin, Developer, GeneralUser

# Create an Admin
admin1 = Admin("Denny Crane")

# Create a Developer
dev1 = Developer("Allan Shore")

# Create a GeneralUser
user1 = GeneralUser("Tiger Woods")

# admin assigning tasks to developer and general user
admin1.assign_task(dev1, "Fix login bug")
admin1.assign_task(user1, "Attend training session")

# developer viewing tasks and pushes code
dev1.view_tasks()
dev1.push_code()

# General User views tasks
user1.view_tasks()

# Admin views their own task list
admin1.view_tasks()

# Add extra tasks directly
dev1.add_task("Go to court for deposition")

user1.view_tasks()