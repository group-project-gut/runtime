from src.actions.action import Action


class Wave(Action):
    """
    Simple action for playing an animation on frontend.
    """

    def __init__(self, agent: 'Agent') -> None:
        super().__init__()
        self.properties.agent_id = agent.properties.id

    def execute(self) -> None:
        self.log()
