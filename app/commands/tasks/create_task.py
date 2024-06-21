from app.core.commands import WriteCommand


class CreateTaskCommand(WriteCommand):
    def __init__(self, data):
        pass

    def validate(self) -> bool:
        return True

    def execute(self) -> dict:
        pass
