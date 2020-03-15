import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(200, 200)
        self.x = 125
        self.y = 100
        self.personagem1 = personagem(100,100,3,8)
        pyxel.run(self.update, self.draw)
        self.valor = 0

    def update(self):
      
        if pyxel.btn(pyxel.KEY_D) and self.personagem1.x + 1 < 200:
            self.personagem1.x = self.personagem1.x + 1
        if pyxel.btn(pyxel.KEY_A) and self.personagem1.x - 1 > -1 :
            self.personagem1.x = self.personagem1.x - 1
        if pyxel.btn(pyxel.KEY_S) and self.personagem1.y + 1 < 200 :
            self.personagem1.y = self.personagem1.y + 1
        if pyxel.btn(pyxel.KEY_W) and self.personagem1.y - 1 > -1:
            self.personagem1.y = self.personagem1.y - 1
        if pyxel.btn(pyxel.KEY_SPACE):
            self.personagem1.x = pyxel.mouse_x
            self.personagem1.y = pyxel.mouse_y
        if self.personagem1.x > 200:
            self.personagem1.x = 199
        if self.personagem1.x < 0:
            self.personagem1.x = 0
        if self.personagem1.y > 200:
            self.personagem1.y = 199
        if self.personagem1.y < 0:
            self.personagem1.y = 0
        



            
    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.personagem1.x,self.personagem1.y,3,self.personagem1.cor)



class personagem():
    def __init__(self,x,y,h,cor):
        self.x = x
        self.y = y
        self.h = h
        self.cor = cor







App()
