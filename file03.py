import pyxel
import random


class App:
    def __init__(self):
       
        pyxel.init(100,100)
        self.x = 50
        self.y = 50
        self.cor = 3

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_D) and self.x == 99:
            self.x = 0
        if pyxel.btn(pyxel.KEY_A) and self.x == 0:
            self.x = 99
        if pyxel.btn(pyxel.KEY_W) and self.y == 0:
         self.y = 99
        if pyxel.btn(pyxel.KEY_S) and self.y == 99:
            self.y = 0
        if pyxel.btn(pyxel.KEY_D) and self.x < 100:
            self.x += 1
        if pyxel.btn(pyxel.KEY_A) and self.x > 0:
            self.x -= 1
        if pyxel.btn(pyxel.KEY_W) and self.y > 0:
            self.y -= 1
        if pyxel.btn(pyxel.KEY_S) and self.y < 100:
            self.y += 1


    def draw(self):
        pyxel.cls(self.cor)
        pyxel.circ(self.x,self.y,2,8)


App()
