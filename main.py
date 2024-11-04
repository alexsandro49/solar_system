from ursina import Ursina, Entity, color, time, held_keys, camera, mouse, Text, window, Vec2, Vec3
from ursina.shaders import lit_with_shadows_shader
from ursina.lights import PointLight
from ursina.prefabs.sky import Sky
import numpy as np

app = Ursina(borderless=False, fullscreen=False, development_mode=True, editor_ui_enabled=True)

sky = Sky(color="#000000")  # Certifique-se de que o céu é uma entidade independente
PointLight()

t = -np.pi

# Define o Sol com 'collider' e 'info'
sun = Entity(
    name='Sol',
    model='sphere',
    scale=1.5,
    texture='textures/sun_texture.jpg',
    collider='sphere',
    info=(
        "O Sol é a estrela no centro do Sistema Solar. "
        "É uma esfera quase perfeita de plasma quente, gerando energia através de fusão nuclear de hidrogênio em hélio em seu núcleo. "
        "Essa energia é essencial para a vida na Terra, fornecendo luz e calor."
    ),
    color=color.white,  # Certifica-se de que a cor não afeta a textura
    shader=lit_with_shadows_shader
)

# Lista para armazenar os corpos celestes (planetas e o Sol)
celestial_bodies = []

# Adiciona o Sol à lista
celestial_bodies.append(sun)

# Função para criar planetas
def create_planet(name, scale, texture, info):
    return Entity(
        name=name,
        model='sphere',
        scale=scale,
        texture=texture,
        collider='sphere',
        info=info,
        color=color.white,  # Certifica-se de que a cor não afeta a textura
        shader=lit_with_shadows_shader
    )

# Define os planetas e adiciona-os à lista
mercury = create_planet(
    name='Mercúrio',
    scale=0.2,
    texture='textures/mercury_texture.jpg',
    info=(
        "Mercúrio é o planeta mais próximo do Sol e o menor do Sistema Solar. "
        "Possui uma superfície repleta de crateras, semelhante à da Lua. "
        "Devido à sua fina atmosfera, experimenta variações extremas de temperatura."
    )
)
celestial_bodies.append(mercury)

venus = create_planet(
    name='Vênus',
    scale=0.3,
    texture='textures/venus_texture.jpg',
    info=(
        "Vênus é o segundo planeta a partir do Sol e é semelhante em tamanho e composição à Terra. "
        "No entanto, possui uma atmosfera densa de dióxido de carbono que cria um efeito estufa intenso, "
        "fazendo dele o planeta mais quente do Sistema Solar."
    )
)
celestial_bodies.append(venus)

earth = create_planet(
    name='Terra',
    scale=0.4,
    texture='textures/earth_texture.jpg',
    info=(
        "A Terra é o terceiro planeta a partir do Sol e o único conhecido por abrigar vida. "
        "Sua atmosfera rica em oxigênio e abundância de água líquida criam condições ideais para a biodiversidade. "
        "Possui um único satélite natural, a Lua."
    )
)
celestial_bodies.append(earth)

mars = create_planet(
    name='Marte',
    scale=0.3,
    texture='textures/mars_texture.jpg',
    info=(
        "Marte é conhecido como o Planeta Vermelho devido ao óxido de ferro em sua superfície, que lhe confere uma coloração avermelhada. "
        "Possui calotas polares e evidências de que água líquida já fluiu em sua superfície."
    )
)
celestial_bodies.append(mars)

jupiter = create_planet(
    name='Júpiter',
    scale=0.6,
    texture='textures/jupiter_texture.jpg',
    info=(
        "Júpiter é o maior planeta do Sistema Solar, um gigante gasoso composto principalmente de hidrogênio e hélio. "
        "É famoso por sua Grande Mancha Vermelha, uma tempestade persistente maior que a Terra."
    )
)
celestial_bodies.append(jupiter)

saturn = create_planet(
    name='Saturno',
    scale=0.5,
    texture='textures/saturn_texture.jpg',
    info=(
        "Saturno é conhecido por seus extensos anéis compostos de gelo e partículas rochosas. "
        "É o segundo maior planeta do Sistema Solar e possui mais de 80 luas conhecidas."
    )
)
celestial_bodies.append(saturn)

uranus = create_planet(
    name='Urano',
    scale=0.5,
    texture='textures/uranus_texture.jpg',
    info=(
        "Urano é um gigante gasoso com a peculiaridade de girar de lado, com seu eixo de rotação quase paralelo ao plano de sua órbita. "
        "Sua atmosfera contém metano, que lhe confere uma tonalidade azul-esverdeada."
    )
)
celestial_bodies.append(uranus)

neptune = create_planet(
    name='Netuno',
    scale=0.5,
    texture='textures/neptune_texture.jpg',
    info=(
        "Netuno é o planeta mais distante do Sol no Sistema Solar. "
        "É semelhante a Urano em composição e cor, devido à presença de metano em sua atmosfera. "
        "Netuno possui os ventos mais rápidos registrados, com velocidades superiores a 2.000 km/h."
    )
)
celestial_bodies.append(neptune)

title_font = "fonts/ChakraPetch-Bold.ttf"
body_font = "fonts/ChakraPetch-Regular.ttf"

# Crie uma entidade de texto para exibir informações
info_text = Text(
    text='',
    position=window.top_left + Vec2(0.02, -0.08),
    origin=(-0.5, 0.5),
    color=color.white,
    background=True,
    scale=0.7,
    font=body_font
)

title_text = Text(
    text='',
    position=window.top_left + Vec2(0.02, -0.02),
    origin=(-0.5, 0.5),
    color=color.white,
    background=True,
    scale=1,
    font=title_font
)

# Adiciona textos auxiliares na parte inferior da tela
helper_text = Text(
    text='Use W, A, S, D para mover a câmera | Use Q para descer e E para subir a câmera | Clique esquerdo para selecionar um astro | Clique direito para mover o ângulo da câmera | Z para visão de cima | ESC para retornar',
    position=window.bottom_left + Vec2(0, 0.02),
    origin=(-0.55, -0.5),
    color=color.white,
    background=True,
    scale=0.6,
    font=body_font
)

# Variável para rastrear o corpo selecionado
selected_body = None

# Variáveis para controle da câmera livre
free_camera_speed = 5
camera_rotation_speed = 100

# Defina a posição e a rotação iniciais da câmera
initial_camera_position = Vec3(0, 10, -20)  # Ajuste conforme necessário
initial_camera_rotation = Vec3(15, 0, 0)    # Ajuste conforme necessário

# Configure a câmera para a posição inicial
camera.position = initial_camera_position
camera.rotation = initial_camera_rotation
camera.look_at(sun.position)

def update():
    global t, selected_body

    angle = np.pi * 40 / 180
    t += 0.01

    # Atualiza as posições dos planetas
    mercury.position = Vec3(np.cos(t) * 1, 0, np.sin(t) * 1)
    venus.position = Vec3(np.cos(t + angle) * 1.4, 0, np.sin(t + angle) * 1.4)
    earth.position = Vec3(np.cos(t + angle * 2) * 1.8, 0, np.sin(t + angle * 2) * 1.8)
    mars.position = Vec3(np.cos(t + angle * 3) * 2.2, 0, np.sin(t + angle * 3) * 2.2)
    jupiter.position = Vec3(np.cos(t + angle * 4) * 2.6, 0, np.sin(t + angle * 4) * 2.6)
    saturn.position = Vec3(np.cos(t + angle * 5) * 3, 0, np.sin(t + angle * 5) * 3)
    uranus.position = Vec3(np.cos(t + angle * 6) * 3.4, 0, np.sin(t + angle * 6) * 3.4)
    neptune.position = Vec3(np.cos(t + angle * 7) * 3.8, 0, np.sin(t + angle * 7) * 3.8)

    if selected_body:
        # Atualiza a posição da câmera para manter o corpo selecionado no centro
        distance = selected_body.scale_y * 5  # Ajuste conforme necessário
        dir_vector = (camera.position - selected_body.position).normalized()
        camera.position = selected_body.position + dir_vector * distance
        camera.look_at(selected_body.position)

        # Exibe as informações do corpo selecionado
        title_text.text = f"{selected_body.name}"
        info_text.text = f"{selected_body.info}"
        info_text.wordwrap=40
    else:
        # Controles da câmera livre
        if held_keys['w']:
            camera.position += camera.forward * free_camera_speed * time.dt
        if held_keys['s']:
            camera.position -= camera.forward * free_camera_speed * time.dt
        if held_keys['a']:
            camera.position -= camera.right * free_camera_speed * time.dt
        if held_keys['d']:
            camera.position += camera.right * free_camera_speed * time.dt
        if held_keys['e']:
            camera.position += camera.up * free_camera_speed * time.dt
        if held_keys['q']:
            camera.position -= camera.up * free_camera_speed * time.dt

        # Rotação da câmera
        if mouse.right:
            camera.rotation_y += mouse.velocity[0] * camera_rotation_speed * time.dt
            camera.rotation_x -= mouse.velocity[1] * camera_rotation_speed * time.dt
            # Limita a rotação vertical para evitar capotamento
            camera.rotation_x = max(min(camera.rotation_x, 90), -90)

        # Limpa o texto quando nenhum astro está selecionado
        info_text.text = ''
        title_text.text = ''

def input(key):
    global selected_body

    
    if key == 'left mouse down':
        if mouse.hovered_entity in celestial_bodies:
            reset_planet_infomation()
            selected_body = mouse.hovered_entity
            focus_on_body(selected_body)

    if key == 'z':
        selected_body = None
        reset_planet_infomation()
        camera.position = Vec3(0, 25, 0)
        camera.look_at(sun.position)

    elif key == 'escape':
        # Retorna ao modo de câmera livre e redefine a posição inicial
        selected_body = None
        reset_planet_infomation()
        camera.look_at(sun.position)
        

def focus_on_body(body):
    # Define a posição da câmera para focar no corpo selecionado
    distance = body.scale_y * 5  # Ajuste conforme necessário
    if body != sun:
        dir_vector = (body.position - sun.position).normalized()
    else:
        dir_vector = Vec3(0, 0, -1)
    camera.position = body.position + dir_vector * distance
    camera.look_at(body.position)

def reset_planet_infomation():
    camera.position = initial_camera_position
    camera.rotation = initial_camera_rotation
    info_text.text = ''
    title_text.text = ''


app.run()
