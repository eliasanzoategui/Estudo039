import pyxel
import random




class App:
    def __init__(self):
        pyxel.init(256,256)
        self.jogador1 = Entidade('jogador',0,0,0,0)
        self.criatura2 = Entidade('criatura',120,120,0,0)
        self.criatura1 = Entidade('criatura',130,130,0,0)
        self.oxigênio = 200
        self.entidades = [self.jogador1,self.criatura1,self.criatura2]
        self.contador = 0
        self.limitador = 10
        self.limite = True
        self.blocos = []
        pyxel.run(self.update,self.draw)

    def update(self):
        if self.jogador1.vivo:
            for i in self.entidades:
                if i.tipo == 'jogador':
                    if i.vivo:
                        i.semover()
                        i.realocar()
                        if self.oxigênio <= 0:
                            i.morto
                        for e in self.entidades:
                            if e.tipo == 'criatura':
                                if i.x == e.x + 1:
                                    e.ex += i.ex
                                    i.ex += e.ex
                                if i.x == e.x - 1:
                                    e.ex += i.ex
                                    i.ex += e.ex
                                if i.y == e.y + 1:
                                    e.ey += i.ey
                                    i.ey += e.ey
                                if i.y == e.y - 1:
                                    e.ey += i.ey
                                    i.ey += e.ey
                                if i.x == e.x:
                                    e.ey += i.ey
                                    i.ey += e.ey

            if i.tipo == 'criatura':
                if i.vivo:
                    i.mover_aleatoriamente()
        self.contador += 1
        if self.contador > self.limitador:
            self.limite = True
            self.contador = 0
        if self.limite:
            self.oxigênio -= 1
            self.limite = False
            if self.oxigênio < 0:
                self.oxigênio = 0

    def draw(self):
        pyxel.cls(0)
        pyxel.text(0,0,str(self.jogador1.x),7)
        pyxel.text(0,20,str(self.jogador1.y),7)
        for i in self.entidades:
            if i.tipo == 'jogador':
                pyxel.rect(128,128,1,1,3)
            if i.tipo == 'criatura':
                pyxel.rect(i.x - self.jogador1.x, i.y - self.jogador1.y,1,1,10)
        pyxel.rect(10,240,self.oxigênio,2,5)






class Bloco():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Entidade():
    def __init__(self,tipo,x,y,ex,ey):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.vivo = True
        self.energia = True
        self.oxigênio = 200
        self.limitador = 50
        self.contador = 0
    def contadormaisum(self):
        self.contador += 1
        if self.contador > self.limitador:
            self.contador = 0
            self.energia = True
    def semover(self):
        if pyxel.btn(pyxel.KEY_UP) and self.energia:
            self.ey -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.energia:
            self.ey += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.energia:
            self.ex -= 1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.energia:
            self.ex += 1
    def mover_aleatoriamente(self):
        numero_aleatorio = random.randint(-2,2)
        self.ex += numero_aleatorio
        numero_aleatorio = random.randint(-2,2)
        self.ey += numero_aleatorio

    def realocar(self):
        self.x += self.ex
        self.y += self.ey
    def morto(self):
        self.vivo = False
    

App()