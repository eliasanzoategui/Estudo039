import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(256, 256)
        self.criatura3 = Entidade('criatura',random.randint(0,255),random.randint(0,255),0,0,50)
        self.fruta1 = Entidade('moeda',random.randint(0,255),random.randint(0,255),0,0,10)
        self.personagem1 = Entidade('personagem',128,128,0,0,10)
        self.entidades = [self.criatura3,self.fruta1,self.personagem1]
        pyxel.run(self.update, self.draw)
        

    def update(self):
        for i in self.entidades:
            if i.tipo == 'personagem':
                if pyxel.btn(pyxel.KEY_UP):
                    i.energiay -= 1
                if pyxel.btn(pyxel.KEY_DOWN):
                    i.energiay += 1
                if pyxel.btn(pyxel.KEY_LEFT):
                    i.energiax -= 1
                if pyxel.btn(pyxel.KEY_RIGHT):
                    i.energiax += 1
        
                for e in self.entidades:
                    if i.tipo == 'personagem':
                        if e.x > i.x and e.posiçãox and e.tipo == 'criatura':
                            e.energiax -= 1
                            e.posiçãox = False
                        if e.x < i.x and e.posiçãox and e.tipo == 'criatura':
                            e.energiax += 1
                            e.posiçãox = False
                        if e.y > i.y and e.posiçãoy and e.tipo == 'criatura':
                            e.energiay -= 1
                            e.posiçãoy = False
                        if e.y < i.y and e.posiçãoy and e.tipo == 'criatura':
                            e.energiay += 1
                            e.posiçãoy = False

                                 
                               
                           
            if i.energiax > 10:
                i.energiax = 9
            if i.energiax < -10:
                i.energiax = -9
            if i.energiay > 10:
                i.energiay = 9
            if i.energiay < -10:
                i.energiay = -9        
            i.contadormaisum()
            i.realocarposição()
            if i.y > 255:
                i.y = 0
            if i.y < 0:
                i.y = 256
            if i.x > 255:
                i.x = 0
            if i.x < 0:
                i.x = 256



            
    def draw(self):
        pyxel.cls(0)
        for i in self.entidades:
            if i.tipo == 'personagem':
                pyxel.rectb(i.x,i.y,1,1,11)
            if i.tipo == 'criatura':
                pyxel.rect(i.x,i.y,1,1,9)
            if i.tipo == 'moeda':
                pyxel.rect(i.x,i.y,1,1,10)
              



class Entidade():
    def __init__(self,tipo,x,y,energiax,energiay,limitador):
        self.contador = 0
        self.limitador = limitador
        self.posiçãox = True
        self.posiçãoy = True
        self.modo = 'neutro'
        self.tipo = tipo
        self.x = x
        self.y = y
        self.energiax = energiax
        self.energiay = energiay
    def realocarposição(self):
        self.x += self.energiax
        self.y += self.energiay
    def contadormaisum(self):
        self.contador += 1
        if self.contador > self.limitador:
            self.posiçãox = True
            self.posiçãoy = True
            self.contador = 0
    def modo(self,modo):
        self.modo = modo


        


App()
