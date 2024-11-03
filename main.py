from ursina import (
    Ursina,
    Entity,
    Sky,
    EditorCamera,
    scene,
    camera,
)
from piece_cube import PieceCube
from rubik_cube import RubikCube

app = Ursina(
    borderless=False, fullscreen=False, development_mode=True, editor_ui_enabled=True
)

Sky()
EditorCamera()

MODEL = "models/custom_cube.obj"
TEXTURE = "textures/rubik_texture.png"

PARENT = PieceCube(
    model=MODEL,
    position=(0, 0, 0),
    texture="noise",
)

rubik_cube = RubikCube(PARENT)


piece_positions = [
    (-1, -1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (0, -1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (1, -1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (-1, 0, -1),
    (0, 0, -1),
    (1, 0, -1),
    (-1, 0, 0),
    (1, 0, 0),
    (-1, 0, 1),
    (0, 0, 1),
    (1, 0, 1),
    (-1, 1, -1),
    (0, 1, -1),
    (1, 1, -1),
    (-1, 1, 0),
    (0, 1, 0),
    (1, 1, 0),
    (-1, 1, 1),
    (0, 1, 1),
    (1, 1, 1),
]


for piece_position in piece_positions:
    cube = PieceCube(
        model=MODEL,
        texture=TEXTURE,
        parent=scene,
        position=piece_position,
    )

    rubik_cube.add_piece(cube)

Entity(
    model="quad",
    scale=60,
    texture="white_cube",
    texture_scale=(60, 60),
    rotation_x=90,
    y=-5,
)

camera.position = (0, 0, 0)

app.run()
