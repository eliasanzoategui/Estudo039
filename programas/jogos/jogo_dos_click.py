import random
import pyxel


class Nuvem():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def update(self):
        self.y += 1


class App :
    def __init__(self):
        pyxel.init( 160 , 120 )
        pyxel.run(self.update,self.draw)
        self.entidades = []
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn("MOUSE_LEFT_BOTTON"):
            nuvem = Nuvem(pyxel.mouse_x,pyxel.mouse_y)
            self.entidades
        for i in self.entidades:
            i.update()
            if i.y > 256:
                self.entidades.remove(i)
    def draw(self):
         pyxel.cls(0)
         pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,7)
         for i in self.entidades:
             pyxel.rect(i.x,i.y,1,1,5)
 

App()