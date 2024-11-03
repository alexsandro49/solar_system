from ursina import Ursina, Entity, Sky, EditorCamera, color, scene

app = Ursina(
  fullscreen=False,
  development_mode=True,
  editor_ui_enabled=True
)

Sky()
EditorCamera()

MODEL = 'models/custom_cube.obj'
TEXTURE = 'textures/rubik_texture.png'

ROTATE=0

PARENT = Entity(
  model=MODEL,
  position=(0, 0, 0),
  texture='noise',
)

def generate_cube_positions():
  positions = [
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
  
  return positions


CUBE_POSITIONS = generate_cube_positions()
CUBES = []

for cube_position in CUBE_POSITIONS:
  cube = Entity(
    model=MODEL,
    texture=TEXTURE,
    parent=scene,
    position=cube_position,
  )
  
  CUBES.append(cube)

def get_cubes_to_rotate(line=None, col=None):
    # Verifica se tanto linha quanto coluna foram informados
    if line is not None and col is not None:
        raise ValueError("Informe apenas uma linha ou uma coluna, nunca os dois.")

    cubes = []

    for cube in CUBES:
        # Verifica se a linha ou a coluna corresponde ao cubo atual
        if (line is not None and cube.position[1] == line) or \
           (col is not None and cube.position[0] == col):
            cubes.append(cube)

    return cubes

def reparent_to_parent(cubes):
  for cube in cubes:
    cube.parent = PARENT
    
def reparent_to_scene():
  for cube in CUBES:
   if cube.parent == PARENT:
    world_pos, world_rot = round(cube.world_position, 1), cube.world_rotation
    cube.parent = scene
    cube.position, cube.rotation = world_pos, world_rot

  PARENT.rotation_x, PARENT.rotation_y = 0, 0

def input(key):
  global ROTATE
  
  if key == 'left arrow up':
    reparent_to_scene()
    cubes = get_cubes_to_rotate(line=0)
    reparent_to_parent(cubes)
    ROTATE += 90
    PARENT.animate_rotation_y(ROTATE, duration=0.5)
    ROTATE=0

  elif key == 'up arrow up':
    reparent_to_scene()
    cubes = get_cubes_to_rotate(col=0)
    reparent_to_parent(cubes)
    ROTATE += 90
    PARENT.animate_rotation_x(ROTATE, duration=0.5)
    ROTATE=0
  
 
  # elif key == 'w':
  #   world_pos, world_rot = round(CUBE.world_position, 1), CUBE.world_rotation
  #   CUBE.parent = scene
  #   CUBE.position, CUBE.rotation = world_pos, world_rot
  # elif key == 's':
  #   ROTATE_X, ROTATE_Y = 0, 0
  #   PARENT.rotation_x, PARENT.rotation_y = 0, 0
  #   CUBE.parent = PARENT
  


Entity(model="quad", scale=60, texture='white_cube', texture_scale=(60, 60), rotation_x=90, y=-5) # plano




app.run()