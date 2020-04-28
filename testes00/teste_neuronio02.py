
def neuronio(entrada,peso,bias): 
    return entrada * peso + bias


class Neuronio():
    def __init__(self,peso,bias,limiar,proximo_neuronio):
        self.peso = peso
        self.bias = bias
        self.limiar = limiar
        self.camada = 0
    def ativar(entrada):
        if self.camada > self.limiar:
            self.proximo_neuronio.entrada(self.camada)
    def entrada(self,entrada):
        self.camada += entrada
    




neuronio1 = Neuronio(10,10,20)

neuronio2 = Neuronio(0.5,-20,20)







