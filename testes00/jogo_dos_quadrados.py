import pyxel
import random

# o jogo em si

class jogo():
    def __init__(self):
        pyxel.init(256,256)
        self.fruta1 = Entidade('fruta',random.randint(0,255),random.randint(0,255),8)
        self.criatura1 = Entidade('criatura',100,100,9)
        self.jogador1 = Entidade('jogador',128,128,3)
        self.entidades = [self.jogador1,self.criatura1,self.fruta1]
        pyxel.run(self.update,self.draw)

# atualiza o jogo dependendo do tipo da entidade

    def update(self):
        for i in self.entidades:
        # tipo criatura
            i.y += 1
            if i.tipo == 'criatura':
                i.moveraleatoriamente()
                if i.x + 5 > 256:
                  i.x  = 256 - 5
                if i.x - 5 < 0:
                    i.x = 0 + 5
                if i.y + 5 > 256:
                    i.y = 256 - 5
                if i.y - 5 < 0:
                    i.y = 0 + 5
        # tipo jogador
            if i.tipo == 'jogador':
                if pyxel.btnp(pyxel.KEY_UP):
                    i.y -= 10
                if pyxel.btn(pyxel.KEY_DOWN):
                    i.y += 1
                if pyxel.btn(pyxel.KEY_LEFT):
                    i.x -= 1
                if pyxel.btn(pyxel.KEY_RIGHT):
                    i.x += 1
                if i.x + 10 > 256:
                  i.x  = 256 - 10
                if i.x - 10 < 0:
                    i.x = 0 + 10
                if i.y + 10 > 256:
                    i.y = 256 - 10
                if i.y - 10 < 0:
                    i.y = 0 + 10
            if i.tipo == 'fruta':
                if i.x + 2 > 256:
                    i.x  = 256 - 2
                if i.x - 2 < 0:
                    i.x = 0 + 2
                if i.y + 2 > 256:
                    i.y = 256 - 2
                if i.y - 2 < 0:
                    i.y = 0 + 2




# desenha os itens na tela
    def draw(self):
        pyxel.cls(7)
        for i in self.entidades:
            if i.tipo == 'jogador':
                pyxel.rect(i.x - 10,i.y - 10,20,20,i.cor)
            if i.tipo == 'criatura':
                pyxel.rect(i.x - 5,i.y - 5,10,10,9)
            if i.tipo == 'fruta':
                pyxel.rect(i.x - 2, i.y -2,4,4,i.cor)

# clases 

class Entidade():
    def __init__(self,tipo,x,y,cor):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.cor = cor
    def moveraleatoriamente(self):
        númeroaleatório = random.randint(0,3)
        if númeroaleatório == 0:
            self.x -= 1
        if númeroaleatório == 1:
            self.x += 1
        if númeroaleatório == 2:
            self.y -= 1
        if númeroaleatório == 3:
            self.y += 1

jogo()