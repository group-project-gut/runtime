from abc import ABC, abstractmethod


class StateMachine(ABC):
    def __init__(self):
        self._state = None
        self._previous_state = None
        self._states = {}

    @abstractmethod
    def _state_logic(self):
        pass

    @abstractmethod
    def _get_transition(self):
        return None

    @abstractmethod
    def _enter_state(self, new_state, old_state):
        pass

    @abstractmethod
    def _exit_state(self, old_state, new_state):
        pass

    def set_state(self, new_state):
        self._previous_state = self._state
        self._state = new_state
        if self._previous_state:
            self._exit_state(self._previous_state, new_state)
        if new_state:
            self._enter_state(new_state, self._previous_state)

    def add_state(self, name):
        self._states[name] = name

    def tick(self):
        if self._state:
            self._state_logic()
            transition = self._get_transition()
            if transition:
                self.set_state(transition)
