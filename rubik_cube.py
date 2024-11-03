from ursina import Entity, scene


class RubikCube(Entity):
    def __init__(self, core_piece):
        super().__init__()
        self.core_piece = core_piece
        self.pieces = []
        self.ROTATE = 0

    def add_piece(self, piece):
        self.pieces.append(piece)

    def reparent_to_parent(self, cubes):
        for cube in cubes:
            cube.parent = self.core_piece

    def reparent_to_scene(self):
        for cube in self.pieces:
            if cube.parent == self.core_piece:
                world_pos, world_rot = (
                    round(cube.world_position, 1),
                    cube.world_rotation,
                )
                cube.parent = scene
                cube.position, cube.rotation = world_pos, world_rot

        self.core_piece.rotation_x, self.core_piece.rotation_y = 0, 0

    def get_cubes_to_rotate(self, line=None, col=None):
        # Verifica se tanto linha quanto coluna foram informados
        if line is not None and col is not None:
            raise ValueError("Informe apenas uma linha ou uma coluna, nunca os dois.")

        cubes = []

        for cube in self.pieces:
            # Verifica se a linha ou a coluna corresponde ao cubo atual
            if (line is not None and cube.position[1] == line) or (
                col is not None and cube.position[0] == col
            ):
                cubes.append(cube)

        return cubes

    def input(self, key):
        if key == "left arrow up":
            self.reparent_to_scene()
            cubes = self.get_cubes_to_rotate(line=0)
            self.reparent_to_parent(cubes)
            self.ROTATE += 90
            self.core_piece.animate_rotation_y(self.ROTATE, duration=0.5)
            self.ROTATE = 0

        elif key == "up arrow up":
            self.reparent_to_scene()
            cubes = self.get_cubes_to_rotate(col=0)
            self.reparent_to_parent(cubes)
            self.ROTATE += 90
            self.core_piece.animate_rotation_x(self.ROTATE, duration=0.5)
            self.ROTATE = 0
