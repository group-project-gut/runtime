import json

# Properties is an empty class
# used by objects inheriting from Serialzable
# to store variables that will be serialized


class Properties:
    def __init__(self) -> None:
        pass


class Serializable():
    def __init__(self, base: str) -> None:
        self.base = base
        self.properties = Properties()

    def __str__(self) -> str:
        return f"{{ \"base_class_name\" : \"{self.base}\", \"class_name\" : \"{self.__class__.__name__}\", \"properties\" : {json.dumps(self.properties.__dict__, default=str)} }}"
