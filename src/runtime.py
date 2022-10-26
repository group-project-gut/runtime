from .agent import Agent
from .enums import Direction


class Runtime:
    max_spins: int = 128

    def __init__(self, agents_code: str) -> None:
        self.agents_code: str = agents_code

    def run(self) -> None:
        agent = Agent((0,0))
        agent_locals = {}
        agent_builtins = {
            'move': agent.move,
            'Direction': Direction,
        }
        spins = 0
        while spins < self.max_spins:
            exec(
                self.agents_code,
                agent_builtins,
                agent_locals,
            )
            #print(agent)
            spins += 1
