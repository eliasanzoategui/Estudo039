import random

class neuronio():
    def __init__(self,direcao_limiar,direcao,direcao_bias,limiar,peso,bias,taxa_de_apreendizado,camada):
        self.direcao_bias = None
        self.direcao = None
        self.direcao_limiar = None
        self.camada = camada
        if self.direcao_limiar == 'mais':
            self.direcao_limiar = 'mais'
        if self.direcao_limiar == 'menos':
            self.direcao_limiar = 'menos'
        if self.direcao_limiar == 'aleatório':
            self.direcao_limiar = 'aleatório'
        if direcao == 'mais':
            self.direcao = 'mais'
        if direcao == 'menos':
            self.direcao = 'menos'
        if direcao == 'aleatório':
            self.direcao = 'aleatório'
        if direcao_bias == 'mais':
            self.direcao_bias = 'mais'
        if direcao_bias == 'menos':
            self.direcao_bias = 'menos'
        if direcao_bias == 'aleatório':
            self.direcao_bias = 'aleatório'
        self.limiar = limiar
        self.peso = peso
        self.bias = bias
        self.taxa = taxa_de_apreendizado
    def trocar_direcao(self):
        num = random.randint(0,2)
        if num == 0:
            self.direcao = 'mais'
        if num == 1:
            self.direcao = 'menos'
        if num == 2:
            self.direcao = 'aleatório'
        num = random.randint(0,2)
        if num == 0:
            self.direcao_bias = 'mais'
        if num == 1:
            self.direcao_bias = 'menos'
        if num == 2:
            self.direcao_bias = 'aleatório'
        num = random.randint(0,2)
        if num == 0:
            self.direcao_limiar = 'mais'
        if num == 1:
            self.direcao_limiar = 'menos'
        if num == 2:
            self.direcao_limiar = 'aleatório'
    def atualizar(self):
        if self.direcao == 'mais':
            self.peso += self.taxa
        if self.direcao == 'menos':
            self.peso -= self.taxa
        if self.direcao == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.peso += self.taxa*self.limiar
            if num == 1:
                self.peso -= self.taxa*self.limiar
        if self.direcao_bias == 'mais':
            self.bias += self.taxa
        if self.direcao_bias == 'menos':
            self.bias -= self.taxa
        if self.direcao_bias == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.bias += self.taxa
            if num == 1:
                self.bias -= self.taxa
        if self.direcao_limiar == 'mais':
            self.limiar += self.taxa
        if self.direcao_limiar == 'menos':
            self.limiar -= self.taxa
        if self.direcao_limiar == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.limiar += self.taxa
            if num == 1:
                self.limiar -= self.taxa
    def exercicio(self,entrada,resultado):
        self.camada += entrada*self.peso
        self.camada += self.bias
        if  self.camada >= self.limiar:
            resultado1 = True
        else:
            resultado1 = False
        if resultado1 == resultado:
            self.atualizar()
        else:
            self.trocar_direcao() 

    def execucao(self,entrada,texto1,texto2):
        self.camada += entrada*self.peso
        self.camada += self.bias
        if self.camada > self.limiar:
            print(texto1)
        else:
            print(texto2)





        







