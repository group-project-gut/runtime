objects = look(Direction.NORTH)
if len(objects) == 1 and "Floor" in objects:
    move(Direction.NORTH)
