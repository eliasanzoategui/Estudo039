import pyxel



class Jogador():
    def __init__(self,vida,x,y,energia_orizontal,energia_vertical):
        self.tipo = 'jogador'
        self.vida = vida
        self.x = x
        self.y = y
        self.energia_orizontal = energia_orizontal
        self.energia_vertical = energia_vertical
    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_UP):
            self.x += 1


pyxel.init(256,256)
jogador1 = Jogador(100,128,128,0,0)
entidades = [jogador1]


def update():
    if pyxel.btn(pyxel.KEY_Q):
        pyxel.quit()
    camera_x = jogador1.x - 128
    camera_y = jogador1.y - 128

def draw():
    pyxel.cls(0)
    for i in entidades:
        if i.tipo == 'jogador':
            pyxel.rect(i.x - camera_x,i.y - camera_y,1,1,10)

    

pyxel.run(update,draw)