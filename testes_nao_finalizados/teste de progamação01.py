



class neuronio():
    def __init__(self,peso,bias,limiar,self.taxa_de_apreendisado):
        self.ultima_alteração = 0
        self.taxa_de_apreendisado = self.taxa_de_apreendisado
        self.limiar = limiar
        self.peso = peso
        self.bias = bias
        self.melhorando = False
        self.taxa_de_erro_anterior = 0
        self.taxa_de_erro = 0
        self.saida = 0
    def ativação(entrada,resultado):
        self.taxa_de_erro_anterior = self.taxa_de_erro
        x = 0
        for i in entrada:
            camada += i * self.peso[x]
            x += 1
        camada += self.bias
        if self.camada > self.limiar:
            self.saida = self.camada
        if self.camada <= self.limiar:
            self.saida = 0
        if saida > resultado:
            self.taxa_de_erro = self.saida - resultado
        elif saida == resultado:
            self.taxa_de_erro = 0
        else:
            self.taxa_de_erro = resultado - self.saida
        self.verificar_melhora()
        

    def verificar_melhora():
        if self.taxa_de_erro_anterior < self.taxa_de_erro:
            self.melhorando = False
        elif self.taxa_de_erro == self.taxa_de_erro_anterior:
            self.melhorando = False
        else:
            self.melhorando = True
            
    def ajustar_peso():
        for i in self.peso:
            if self.melhora:
                i += ultima_alteração
            else:
                i -= ultima_alteração
            

        
        