class Task:

    def __init__(self, name, priority, duration):
        self.name = name
        self.priority = priority
        self.duration = duration
        self.started = False
        self.completed = False #no task completed yet

    def start(self):
        """
        Mark the task as started. If it has begun, let the user know.
        """
        if not self.started:
            self.started = True
            print(f"🔄 Task '{self.name}' has now started.")
        else:
            print(f"❗ Task '{self.name}' is already in progress.")

    def complete(self):
        """
        Mark the task as complete, make sure it had started and it should not be completed twice
        """
        #Check that the task has started
        if not self.started:
            print(f"⚠ Cannot complete task '{self.name}' because it has not begun.")
            return
        #If it isn't completed, complete it
        if not self.complete:
            self.completed = True
            print(f"✅ Task {self.name}' has been completed.")
        else:
            #If someone tries to complete it again, warn them
            print(f"❗ Task '{self.name}' was already completed.")

    def update_priority(self, new_priority):
        """
        Change the task's priority to a new level, reporting the change
        """
        old_priority = self.priority
        self.priority = new_priority

        print(f"🔄 Priority for '{self.name}' updated from {old_priority} to {new_priority}.")

    def info(self):
        print("-----  Task Information -----")
        print(f"Name: {self.name}.")
        print(f"Priority: {self.priority}.")
        print(f"Duration: {self.duration} minutes")
        print(f"Started: {'Yes' if self.started else 'No'}")
        print(f"Completed: {'Yes' if self.completed else 'No'}")
        print("------------------------------")

t = Task("Write report", "High", 60)
t.info()
t.start()
t.complete()
t.update_priority("Medium")
t.info()
