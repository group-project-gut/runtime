from src.common.enums import Direction
from src.actions.move import Move
from src.scene import Scene


class Runtime:
    '''
    Supplies basic execution of users code across various levels.
    '''

    def __init__(self, agents_code: str) -> None:
        self.agents_code: str = agents_code

    def run(self) -> None:
        '''
        Generates a new scene and runs users code for a limited number of spins.
        The heart of the class is `exec` which defines the scope of `__builtins__`
        for user supplied code.
        '''
        
        scene: Scene = Scene()

        agent_locals = {}
        agent_builtins = {
            'move': lambda direction: Move(scene.get_player(), direction).execute(scene),
            'Direction': Direction,
            'len': len,
            'range': range,
            'enumerate': enumerate,
        }

        max_spins: int = 8
        spins = 0
        while spins < max_spins:
            exec(
                self.agents_code,
                {'__builtins__': agent_builtins},
                agent_locals,
            )
            #print(scene.get_player())
            spins += 1
