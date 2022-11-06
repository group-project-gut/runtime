from .agent import Agent
from .enums import Direction


class Runtime:
    MAX_SPINS: int = 8

    def __init__(self, agents_code: str) -> None:
        self.agents_code: str = agents_code

    def run(self) -> None:
        agent = Agent()
        agent_locals = {}
        agent_builtins = {
            'move': agent.move,
            'Direction': Direction,
            'len': len,
            'range': range,
            'enumerate': enumerate,
        }
        spins = 0
        while spins < self.MAX_SPINS:
            exec(
                self.agents_code,
                {'__builtins__': agent_builtins},
                agent_locals,
            )
            spins += 1
