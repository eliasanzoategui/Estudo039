import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(200, 200)
        self.criatura3 = criatura(random.randint(0,199),random.randint(0,199),7)
        self.criatura2 = criatura(random.randint(0,199),random.randint(0,199),3)
        self.criatura1 = criatura(random.randint(0,199),random.randint(0,199),11)
        self.criaturas = [self.criatura1,self.criatura2,self.criatura3]
        self.x = 125
        self.y = 100
        self.personagem1 = personagem(100,100,3,8)
        pyxel.run(self.update, self.draw)
        

    def update(self):
      
        if pyxel.btn(pyxel.KEY_D) and self.personagem1.x + 1 < 200:
            self.personagem1.x = self.personagem1.x + 1
        if pyxel.btn(pyxel.KEY_A) and self.personagem1.x - 1 > -1 :
            self.personagem1.x = self.personagem1.x - 1
        if pyxel.btn(pyxel.KEY_S) and self.personagem1.y + 1 < 200 :
            self.personagem1.y = self.personagem1.y + 1
        if pyxel.btn(pyxel.KEY_W) and self.personagem1.y - 1 > -1:
            self.personagem1.y = self.personagem1.y - 1
        if self.personagem1.x > 200:
            self.personagem1.x = 199
        if self.personagem1.x < 0:
            self.personagem1.x = 0
        if self.personagem1.y > 200:
            self.personagem1.y = 199
        if self.personagem1.y < 0:
            self.personagem1.y = 0
        for i in self.criaturas:
            i.update()
            if pyxel.btn(pyxel.KEY_SPACE):
                i.x = self.personagem1.x
                i.y = self.personagem1.y
        

        



            
    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.personagem1.x,self.personagem1.y,3,self.personagem1.cor)
        for i in self.criaturas:
            pyxel.circ(i.x,i.y,1,i.cor)



class personagem():
    def __init__(self,x,y,h,cor):
        self.x = x
        self.y = y
        self.h = h
        self.cor = cor

class criatura():
    def __init__(self,x,y,cor):
        self.x = x 
        self.y = y
        self.cor = cor
        self.númerox = random.randint(-1,1)
        self.númeroy = random.randint(-1,1)
    def update(self):
        self.númerox = random.randint(-1,1)
        self.númeroy = random.randint(-1,1)
        if self.x + self.númerox > 0 and self.x + self.númerox < 200:
            self.x += self.númerox
        if self.y + self.númeroy > 0 and self.y + self.númeroy < 200:
            self.y += self.númeroy
            
            
    
        
        






App()
