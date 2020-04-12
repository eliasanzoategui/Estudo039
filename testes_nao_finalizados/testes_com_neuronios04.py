


class neuronio():
    def __init__(self,peso,limiar,bias,taxa_de_apreendisado):
        self.peso = peso
        self.limiar = limiar
        self.bias = bias
        self.taxa_de_apreendisado = taxa_de_apreendisado
    
    
    def treino(self,entrada,resultado):
        x = 0
        camada_oculta = 0
        for i in entrada:
            camada_oculta += self.peso[x] * entrada[x]
            x += 1
        saida = camada_oculta + self.bias
        if saida > resultado:
            self.peso = self.peso * self.taxa_de_apreendisado * (saida - resultado)
        elif saida == resultado:
            pass
        else:
            self.peso = self.peso * self.taxa_de_apreendisado * (resultado - saida)
    
    def teste(self,entrada,texto1,texto2):
        x = 0
        for i in entrada:
            camada_oculta += self.peso[x] * entrada[x]
            x += 1
        saida = camada_oculta + self.bias
        if saida > self.limiar:
            print(texto1)
            self.neuronio_de_anexo.teste(saida,texto1,texto2)
        else:
            print(texto2)

    def neuronio_de_anexo(self,neuronio_de_anexo):
        self.neuronio_de_anexo = neuronio_de_anexo



