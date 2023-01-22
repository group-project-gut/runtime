from src.actions.action import Action


class WaitForCode(Action):
    """
    Action blocking execution of the runtime until it reads
    message from `stdin` saying that the `code` was uploaded
    """
    interactive: bool

    def __init__(self, interactive: bool) -> None:
        super().__init__()
        self.interactive = interactive

    def execute(self) -> None:
        if not self.interactive:
            return

        self.log()
        message: str = input()
        if message != "CODE UPLOADED":
            exit(1)
