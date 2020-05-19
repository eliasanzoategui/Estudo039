import random



class Criatura():
    def __init__(self,vida,x,y,cor):
        self.cor = cor
        self.tipo = 'criatura'
        self.vida = vida
        self.x = x
        self.y = y
    def update(self):
        numeroaleatorio = random.randint(-1,1)
        self.x += numeroaleatorio
        numeroaleatorio = random.randint(-1,1)
        self.y += numeroaleatorio
        self.vida -= 1
