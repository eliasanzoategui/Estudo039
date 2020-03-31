import random



class neuro():
    def __init__(self,direção_limiar,direção,direção_bias,limiar,peso,bias,taxa_de_apreendisado,camada):
        self.direção_bias = None
        self.direção = None
        self.direção_limiar = None
        self.camada = camada
        if self.direção_limiar == 'mais':
            self.direção_limiar = 'mais'
        if self.direção_limiar == 'menos':
            self.direção_limiar = 'menos'
        if self.direção_limiar == 'aleatório':
            self.direção_limiar = 'aleatório'
        if direção == 'mais':
            self.direção = 'mais'
        if direção == 'menos':
            self.direção = 'menos'
        if direção == 'aleatório':
            self.direção = 'aleatório'
        if direção_bias == 'mais':
            self.direção_bias = 'mais'
        if direção_bias == 'menos':
            self.direção_bias = 'menos'
        if direção_bias == 'aleatório':
            self.direção_bias = 'aleatório'
        self.limiar = limiar
        self.peso = peso
        self.bias = bias
        self.taxa = taxa_de_apreendisado
    def trocar_direção(self):
        num = random.randint(0,2)
        if num == 0:
            self.direção = 'mais'
        if num == 1:
            self.direção = 'menos'
        if num == 2:
            self.direção = 'aleatório'
        num = random.randint(0,2)
        if num == 0:
            self.direção_bias = 'mais'
        if num == 1:
            self.direção_bias = 'menos'
        if num == 2:
            self.direção_bias = 'aleatório'
        num = random.randint(0,2)
        if num == 0:
            self.direção_limiar = 'mais'
        if num == 1:
            self.direção_limiar = 'menos'
        if num == 2:
            self.direção_limiar = 'aleatório'
    def atualizar(self):
        if self.direção == 'mais':
            self.peso += self.taxa
        if self.direção == 'menos':
            self.peso -= self.taxa
        if self.direção == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.peso += self.taxa*self.limiar
            if num == 1:
                self.peso -= self.taxa*self.limiar
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
        if self.direção_limiar == 'mais':
            self.limiar += self.taxa
        if self.direção_limiar == 'menos':
            self.limiar -= self.taxa
        if self.direção_limiar == 'aleatório':
            num = random.randint(0,1)
            if num == 0:
                self.limiar += self.taxa
            if num == 1:
                self.limiar -= self.taxa
    def exercício(self,entrada,resultado):
        self.camada += entrada*self.peso
        self.camada += self.bias
        if  self.camada >= self.limiar:
            resultado1 = True
        else:
            resultado1 = False
        if resultado1 == resultado:
            self.atualizar()
        else:
            self.trocar_direção() 

    def execução(self,entrada,texto1,texto2):
        self.camada += entrada*self.peso
        self.camada += self.bias
        if self.camada > self.limiar:
            print(texto1)
        else:
            print(texto2)





        







