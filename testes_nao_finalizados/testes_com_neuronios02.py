
# direções , mais, menos, esperar, aleatório
import random

class neuronio():
    def __init__(self,limiar,peso,bias,taxa):
        self.peso = peso
        self.limiar = limiar
        self.bias = bias
        self.taxa = taxa
        self.direção_peso = 'mais'
        self.direção_bias = 'mais'
    def atualizar(self):
        if self.direção_peso == 'mais':
            self.peso += self.taxa
        if self.direção_peso == 'menos':
            self.peso -= self.taxa
        if self.direção_peso == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.peso += self.taxa
            if num == 1:
                self.peso -= self.taxa
        if self.direção_bias == 'mais':
            self.bias += self.taxa
        if self.direção_bias == 'menos':
            self.bias -= self.taxa
        if self.direção_bias == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.bias += self.taxa
            if num == 1:
                self.bias -= self.taxa
    def trocar(self):
        num = random.randint(0,3)
        if num == 0:
            self.direção_peso = 'mais'
        if num == 1:
            self.direção_peso = 'menos'
        if num == 2:
            self.direção_peso = 'esperar'
        if num == 3:
            self.direção_peso = 'aleatório'
        num = random.randint(0,3)
        if num == 0:
            self.direção_bias = 'mais'
        if num == 1:
            self.direção_bias = 'menos'
        if num == 2:
            self.direção_bias = 'esperar'
        if num == 3:
            self.direção_bias = 'aleatório'
    def teste(self,entrada,resultado):
        self.camada = entrada * self.peso
        self.camada += self.bias
        if self.camada > self.limiar:
            saída = True
        else:
            saída = False
        if saída != resultado:
            self.trocar()
        else:
            self.atualizar()
    def execução(self,entrada,texto1,texto2):
        self.camada = entrada * self.peso
        self.camada += self.bias
        if self.camada > self.limiar:
            print(texto1)
        else:
            print(texto2)
    