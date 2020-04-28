


class neuronio():
    def __init__(self,pesos,bias,entrada,saida,limiar):
        self.pesos = pesos
        self.bias = bias
        self.entrada = [entrada]
        self.saida = [saida]
        x = 0
        for i in entrada:
            x+=1
        self.divisor = x
        self.camada_de_saida = 0
    def entrada(self,entrada):
        x = 0
        for i in entrada:
            self.camada_de_saida += i *self.pesos[x] + self.bias[x]
            x += 1
    def ativação(self):
        for i in self.saida:
            i.entrada(self.camada_de_saida)






        