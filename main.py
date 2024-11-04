from ursina import Ursina, Entity, EditorCamera, color, time
from ursina.prefabs.sky import Sky
import numpy as np

app = Ursina(borderless=False, fullscreen=False, development_mode=True, editor_ui_enabled=True)

EditorCamera()
Sky()

t = -np.pi



sun = Entity(model='sphere', scale=1.5)

mercury = Entity(model='sphere', scale=0.2)
venus = Entity(model='sphere', scale=0.3)
earth = Entity(model='sphere', scale=0.4)
mars = Entity(model='sphere', scale=0.3)
jupiter = Entity(model='sphere', scale=0.6)
saturn = Entity(model='sphere', scale=0.5)
uranus = Entity(model='sphere', scale=0.5)
neptune = Entity(model='sphere', scale=0.5)

def update():
    global t
    angle = np.pi*40/180

    t += 0.01 #* time.dt

    mercury.x = np.cos(t) * 1
    mercury.z = np.sin(t) * 1

    venus.x = np.cos(t+angle)* 1.4
    venus.z = np.sin(t+angle)* 1.4    

    earth.x = np.cos(t+angle*2)* 1.8
    earth.z = np.sin(t+angle*2)* 1.8

    mars.x = np.cos(t+angle*3)*2.2
    mars.z = np.sin(t+angle*3)*2.2

    jupiter.x = np.cos(t+angle*4)*2.6
    jupiter.z = np.sin(t+angle*4)*2.6
    
    saturn.x = np.cos(t+angle*5)* 3
    saturn.z = np.sin(t+angle*5)* 3  

    uranus.x = np.cos(t+angle*6)* 3.4
    uranus.z = np.sin(t+angle*6)* 3.4  

    neptune.x = np.cos(t+angle*7)* 3.8
    neptune.z = np.sin(t+angle*7)* 3.8  

app.run()