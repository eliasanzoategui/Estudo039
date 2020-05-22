import pyxel
import classe
import random

def save(lista,filename):
    arquivo = open(filename,'w')
    arquivo.seek(0)
    arquivo.write('import classe\n')
    arquivo.write('import random\n')
    arquivo.write('entidades = []\n')
    for i in lista:
        arquivo.write('criatura = classe.Criatura(')
        arquivo.write(str(i.vida))
        arquivo.write(',')
        arquivo.write(str(i.x))
        arquivo.write(',')
        arquivo.write(str(i.y))
        arquivo.write(',')
        arquivo.write(str(i.cor))
        arquivo.write(')\n')
        arquivo.write('entidades.append(criatura)\n')
        arquivo.close









class jogo():
    def __init__(self,entidades):
        self.entidades = entidades
        pyxel.init(256,256)
        pyxel.run(self.update,self.draw)
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_S):
            save(self.entidades,'save1.py')
        if pyxel.btnp(pyxel.KEY_D):
            import save1
            self.entidades = save1.entidades
        for i in entidades:
            if i.vida <= 0:
                self.entidades.remove(i)
            i.update()
            
    def draw(self):
        pyxel.cls(0)
        for i in self.entidades:
            if i.tipo == 'criatura':
                pyxel.pset(i.x,i.y,i.cor)


entidades = []
criatura = classe.Criatura(1000,100,100,10)
entidades.append(criatura)
criatura = classe.Criatura(1000,110,110,8)
entidades.append(criatura)
jogo(entidades)
            

