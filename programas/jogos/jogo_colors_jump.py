import pyxel
import random



class Entidade():
    def __init__(self,x,y,cor,linhagem):
        self.linhagem = linhagem     
        self.x = x
        self.y = y
        self.cor = cor
        self.vida = random.randint(10,500)
    def update(self):
        self.vida -= 1
        numero = random.randint(-1,1)
        self.x += numero
        numero = random.randint(-1,1)
        self.y += numero

        



class jogo():
    def __init__(self,entidades):
        self.tipo = "jogo"
        self.entidades = entidades
        pyxel.init(256,256)
        pyxel.mouse(True)
        pyxel.run(self.update,self.draw)
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            criatura = Entidade(pyxel.mouse_x,pyxel.mouse_y,random.randint(1,15),0)
            self.entidades.append(criatura)       
        for i in self.entidades:
            i.update()
            if i.linhagem > 5:
                self.entidades.remove(i)
            if i.vida <= 0:
                criatura = Entidade(i.x,i.y,random.randint(1,15),i.linhagem+1)
                self.entidades.append(criatura)
                criatura = Entidade(i.x,i.y,random.randint(1,15),i.linhagem+1)
                self.entidades.append(criatura)
                criatura = Entidade(i.x,i.y,random.randint(1,15),i.linhagem+1)
                self.entidades.append(criatura)
                self.entidades.remove(i)
    def draw(self):
        pyxel.cls(0)
        for i in self.entidades:
            pyxel.pset(i.x,i.y,i.cor)


jogo([])