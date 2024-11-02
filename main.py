# Aula sobre animacao - Exercicio 

# 1. Fazer o motor do portao funcionar, rodando as engrenagens. Tecla "L"
# 2. Criar uma sinaleira com duas luzes (laranja e vermelho) pra ficarem piscando alternadamente enquanto o portao abra ou fecha
#    Ex.: http://www.shako.com.br/imagens/predio.jpg
#    Obs.: Pode ficar do mesmo lado do motor.

from math import cos
from math import pi
from math import sin
from math import tan
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global liga_motor
global distancia


esqdir = 0
cimabaixo = 5
aux1 = 0
aux2 = 0
angulo = 60
liga_motor = 0




def eixos():      #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -3.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 6.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -3.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 6.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -3.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 6.0, 4, 10)
    glPopMatrix()

def face_frente():
    # OBJETO cubo branca

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 1, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo vermelho

    glColor3f(1, 0, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 1, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco td

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 1, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo vermelho ml

    glColor3f(1, 0, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 0.5, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()


    # OBJETO cubo branco c

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 0.5, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()


    # OBJETO cubo vermelho md

    glColor3f(1, 0, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 0.5, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()


    # OBJETO cubo branco bl

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 0, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo vermelho bc

    glColor3f(1, 0, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 0, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco bd

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 0, 0)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

def face_esquerda():
    # OBJETO cubo azul tc

    glColor3f(0, 0, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 1, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco te

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 1, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco c

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 0.5, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo azul me

    glColor3f(0, 0, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 0.5, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo azul bc

    glColor3f(0, 0, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 0, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco be

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.5, 0, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

def face_direita():
    # OBJETO cubo verde tc

    glColor3f(0, 1, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 1, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco td

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 1, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco mc

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 0.5, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo verde md

    glColor3f(0, 1, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 0.5, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo verde bc

    glColor3f(0, 1, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 0, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco bd

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.5, 0, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

def face_tras():
    # OBJETO cubo amarelo tc

    glColor3f(1, 1, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 1, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo branco mc

    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 0.5, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

    # OBJETO cubo amarelo bc

    glColor3f(1, 1, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 0, -1)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

def face_topo_e_baixo():
    # OBJETO cubo azul claro tc

    glColor3f(0, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 1, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()


    # OBJETO cubo azul claro pc

    glColor3f(0, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0, 0, -0.5)  #Transtacao do objeto
    # glScale(25, 20, 1)
    #glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glutSolidCube(0.5)
    glPopMatrix()

def desenho():

    eixos()

    face_frente()
    face_esquerda()
    face_direita()
    face_tras()
    face_topo_e_baixo()


def iluminacao_da_cena():
    global aux1
    luzAmbiente=[0.4,0.4,0.4,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[aux1, 50.0, 50.0, 1.0]

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela sera preta
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Habilita o modelo de colorizacao de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletancia do material
    glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, especularidade)
    #  Define a concentracao do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parametros da luz de numero 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

    # Habilita a definicao da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminacao
    glEnable(GL_LIGHTING)
    # Habilita a luz de numero 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    global angulo
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projecao
    glLoadIdentity()# carrega a matriz identidade

    #gluPerspective(angulo, aspecto , near, far )
    #  angulo = angulo em graus na direcao y.
    #  aspecto = deformacao da janela. normalmente e a razao entre a largura e altura
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    gluPerspective(angulo,1,0.1,500) # Especifica a projecao perspectiva

    #glOrtho(left,right,bottom, top, near, far)
    #  left,right,bottom, top = limites da projecao
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado 
    #glOrtho(-5,5,-5,5,0.1,500) # Especifica a projecao paralela ortogonal

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posicao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posicao vertical da camera.
    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posicao do observador e do alvo
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho

# Funcao callback chamada para gerenciar eventos de teclas normais 
def Teclado (tecla, x, y):
    global aux1
    global aux2
    global liga_motor
    
    
    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)
	
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print ("aux1 = ", aux1 )
	
    if tecla == b's': # S
        aux1 = aux1 + 0.1
        print ("aux1 = ", aux1 )
        
    if tecla == b'w': # W
        aux2 = aux2 + 0.1
        print ("aux2 = ", aux2 )

    if tecla == b'z': # Z
        aux2 = aux2 - 0.1
        print ("aux2 = ", aux2 )

    if tecla == b'l': # L
        if (liga_motor == 0):
            liga_motor = 1
        else:
            liga_motor = 0     
        print ("Pressionou o interruptor do motor" )
        
    tela()
    glutPostRedisplay()

# Funcao callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    #print("*** Tratamento de teclas especiais")
    #print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.1
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.1
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()   

# Funcao callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
            if (angulo >= 10):
                angulo -= 2
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()



glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(800,800)
glutCreateWindow(b"Aula10 - Exercicio Animacao")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laco de eventos da GLUT