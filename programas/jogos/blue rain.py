import pyxel
import random

class Entidade():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class jogo():
    def __init__(self):
        pyxel.init(256,256)
        self.entidades = []
        pyxel.run(self.update,self.draw)

    def update(self):
        entidade = Entidade(random.randint(0,256),random.randint(0,30))
        self.entidades.append(entidade)
        self.entidades
        for i in self.entidades:
            i.y += 1
            if i.y > 256:
                self.entidades.remove(i)



    def draw(self):
        pyxel.cls(7)
        for i in self.entidades:
            pyxel.rect(i.x,i.y,1,1,5)
        pyxel.text(10,10,'-CHUVA AZUL-',5)




jogo()