from .objects.object import Object

class Scene():
    def __init__(self) -> None:
        self.objects = {}

    def __getitem__(self, indices) -> Object:
        return self.objects.get(indices)

    def add_object(self, new_object: Object) -> None:
        if self.objects.get(new_object.properties.position) is None:
            self.objects[new_object.properties.position] = [new_object]
        else:
            self.objects[new_object.properties.position].append(new_object)
        print(new_object)