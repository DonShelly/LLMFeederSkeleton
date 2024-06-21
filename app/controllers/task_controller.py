from app.commands.tasks import CreateTaskCommand
from app.controllers.controller import Controller


class TaskController(Controller):
    def create_task(self, data):
        return self.executor.execute_write(CreateTaskCommand(data))
