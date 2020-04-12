
class Neuronio():
    def __init__(self,neuronios_de_anexo,limiar,peso,bias,taxa_de_apreendisado):
        self.neuronios_de_anexo = neuronios_de_anexo
        self.limiar = limiar
        self.peso = peso
        self.bias = bias
        self.taxa_de_apreendisado = taxa_de_apreendisado
    def teste(entrada,resultado):
        qual = 0
        for i in entrada:
            self.camada += i*self.peso[x]
            x += 1
        if self.camada >= self.limiar:
            saida = self.camada
        else:
            saida = 0
        if self.saida == resultado:
            self.sucesso()
        else:
            self.erro()
    

