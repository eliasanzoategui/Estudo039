



class neuronio():
    def __init__(self,peso,bias,limiar,taxa_de_aprendizado):
        self.peso = peso
        self.bias = bias
        self.limiar = limiar
        self.taxa_de_aprendizado = taxa_de_aprendizado

    def treino(self,entrada,resultado):
        camada_oculta = entrada * self.peso
        camada_oculta += self.bias
        if camada_oculta > self.limiar:
            saida = camada_oculta
        else:
            saida = 0
        if saida > resultado:
            self.peso -= self.taxa_de_aprendizado
        elif saida == resultado:
            pass
        else:
            self.peso += self.taxa_de_aprendizado

    def teste(self,entrada,texto1,texto2):
        camada_oculta = entrada * self.peso
        camada_oculta += self.bias
        if camada_oculta > self.limiar:
            print(texto1)
        else:
            print(texto2)
        






neuronio1 = neuronio(1,1,0,0.5)

for i in range(0,100):
    neuronio1.treino(1,0)
    neuronio1.treino(2,1)
    neuronio1.treino(3,0)
    neuronio1.treino(4,1)
    neuronio1.treino(5,0)
    neuronio1.treino(6,1)
    neuronio1.treino(7,0)
    neuronio1.treino(8,1)
    neuronio1.treino(9,0)
    neuronio1.treino(10,1)


neuronio1.teste(7,'é par','é impar')