



class neuronio():
    def __init__(self,peso,bias,limiar,taxa_de_apreendisado):
        self.peso = peso
        self.bias = bias
        self.limiar = limiar
        self.taxa_de_apreendisado = taxa_de_apreendisado

    def treino(self,entrada,resultado):
        camada_oculta = entrada * self.peso
        camada_oculta += self.bias
        if camada_oculta > self.limiar:
            saida = camada_oculta
        else:
            saida = 0
        if saida > resultado:
            self.peso = self.peso * (saida - resultado)
            self.bias = self.bias * (saida - resultado)
        elif saida == resultado:
            pass
        else:
            self.peso = self.peso * (resultado - saida)
            self.bias = self.bias * (resultado - saida)

    def teste(self,entrada,texto1,texto2):
        camada_oculta = entrada * self.peso
        camada_oculta += self.bias
        if camada_oculta > self.limiar:
            print(texto1)
        else:
            print(texto2)
        






neuronio1 = neuronio(1,1,5,0.5)

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


neuronio1.teste(3,'é par','é impar')