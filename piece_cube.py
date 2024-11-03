from ursina import Entity, color


class PieceCube(Entity):
    def __init__(self, model, texture, position, parent=None):
        super().__init__()
        self.model= model
        self.texture= texture
        self.parent= parent
        self.position= position

    
