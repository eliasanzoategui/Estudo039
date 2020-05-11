import pyxel
import random

class Jogador():
    def __init__(self,vida,x,y):
        self.tipo = 'jogador'
        self.vida = vida
        self.x = x
        self.y = y
    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1

class Criatura():
    def __init__(self,vida,x,y):
        self.tipo = 'criatura'
        self.vida = vida
        self.x = x
        self.y = y
    def update(self):
        numero_aleatorio = random.randint(-1,1)
        self.x += numero_aleatorio
        numero_aleatorio = random.randint(-1,1)
        self.y += numero_aleatorio

class Fruta():
    def __init__(self,x,y):
        self.tipo = 'fruta'
        self.x = x
        self.y = y

pyxel.init ( 256 , 256 )
jogador1 = Jogador(100,0,0)
Entidades = [jogador1]
def update ():
    if jogador1.vida > 0:
        if pyxel.btnp(pyxel. KEY_Q ):
            pyxel.quit ()

        for i in Entidades:
            i.update()

def draw ():
    pyxel.cls(0)
    for i in Entidades:
        if i.tipo == 'personagem':
            pyxel.rect(i.x,i.y,1,1,8)



pyxel.run (update, draw)