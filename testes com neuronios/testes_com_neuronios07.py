import random



class Neuronio():
    def __init__(self,subneuronios,proximo_neuronio,pesos,bias,limiar,taxa_de_aprendisado):
        self.subneuronios = subneuronios
        self.proximo_neuronio = proximo_neuronio
        self.pesos = pesos
        self.bias = bias
        self.limiar = limiar
        self.taxa_de_erro = 0
        self.taxa_de_aprendisado = taxa_de_aprendisado
        self.acertividade = 0

    def treino(self,entrada,resultado):
        x = 0
        camada = 0
        for i in entrada:
            camada += (i*self.pesos[x]) + self.bias[x]
            x += 1
        if camada < self.limiar:
            saida = camada
        elif camada == self.limiar:
            saida = 0
        else:
            saida = 0
        if saida > resultado:
            self.taxa_de_erro = saida - resultado
            self.acertividade = 0

        elif saida == resultado:
            self.taxa_de_erro = 0
            self.acertividade = 1

        else:
            self.taxa_de_erro = resultado - saida
            self.acertividade = 0
           
        self.atualizar()

    def atualizar(self):
        for i in self.pesos:
            x = random.randint(0,1)
            if x == 0:
                i += self.taxa_de_erro * self.taxa_de_aprendisado
            else:
                i -= self.taxa_de_erro * self.taxa_de_aprendisado
        for i in self.bias:
            x = random.randint(0,1)
            if x == 0:
                i += self.taxa_de_erro * self.taxa_de_aprendisado
            else:
                i -= self.taxa_de_erro * self.taxa_de_aprendisado

    def retornar_acertividade(self,entrada):
        x = 0
        camada = 0
        for i in entrada:
            camada += (i*self.pesos[x]) + self.bias[x]
            x += 1
        if camada < self.limiar:
            return True
        elif camada == self.limiar:
            return False
        else:
            return False





neuronio1 = Neuronio(None,None,[0,0,0],[0,0,0],0,0.25)

for i in range(0,1000):
    neuronio1.treino([0,0,1],0)
    neuronio1.treino([0,1,0],1)
    neuronio1.treino([0,1,1],0)
    neuronio1.treino([1,0,0],1)
    neuronio1.treino([1,0,1],0)
    neuronio1.treino([1,1,0],1)
    neuronio1.treino([1,1,1],0)



print(neuronio1.retornar_acertividade([0,0,1]))


