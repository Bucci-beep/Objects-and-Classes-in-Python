# AutomatedTaskScheduler 🗓️

A Python-based simulation of a real-world task scheduling system using Object-Oriented Programming and Inheritance. 
This project demonstrates how different user roles (Admin, Developer, GeneralUser) interact with tasks in a simplified workflow.

### 🔹 User (Base Class)
- Attributes: `name`, `role`, `tasks`
- Methods: `add_task()`, `view_tasks()`

### 🔹 Admin (Inherits from User)
- Auto role: `admin`
- Can assign tasks to other users with `assign_task(user, task)`

### 🔹 Developer (Inherits from User)
- Auto role: `developer`
- Can push code using `push_code()`

### 🔹 GeneralUser (Inherits from User)
- Auto role: `general user`
- Can only view and complete their own tasks

---