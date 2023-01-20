from abc import ABC, abstractmethod


class Transition:
    def __init__(self, from_state, to_state, condition_func):
        self.from_state = from_state
        self.to_state = to_state
        self.condition_func = condition_func


class StateMachine(ABC):
    def __init__(self):
        self._state = None
        self._previous_state = None
        self._states = {}
        self._transitions = {}

    @abstractmethod
    def _state_logic(self):
        pass

    def _get_transition(self):
        for transition in self._transitions[self._state]:
            if transition.condition_func():
                return transition.to_state
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
        self._transitions[name] = []
        return self

    def add_transition(self, from_state, to_state, condition_func):
        self._transitions[from_state].append(Transition(from_state, to_state, condition_func))
        return self

    def tick(self):
        if self._state:
            self._state_logic()
            transition = self._get_transition()
            if transition:
                self.set_state(transition)
