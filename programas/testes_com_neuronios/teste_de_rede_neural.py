import random

def encontrar_taxa_de_erro(resultado_esperado,resultado):
    erro = []
    x = 0
    for i in resultado_esperado:
        erro.append(i[x]-resultado[x])
        x += 1
    return erro

def processar(neuronios,pesos,bias):
    resultado = 0
    x = 0
    for i in neuronios:
        resultado += i*pesos[x]+bias[x]
        x += 1
    return resultado






n1 = float(input('digite a entrada1: '))
n2 = float(input('digite a entrada2: '))
n3 = float(input('digite a entrada3: '))

camda1 = [n1,n2,n3]
pesos1 = [random.random(),random.random(),random.random()]
bias1 = [random.random(),random.random(),random.random()]
pesos2 = [random.random(),random.random(),random.random()]
bias2 = [random.random(),random.random(),random.random()]




n4 = processar(camda1,pesos1,bias1)
n5 = processar(camda1,pesos2,bias2)
camda2 = [n4,n5]
camada_resultado = camda2
print(camada_resultado)
resultado = input('digie o resultado: ')
taxa_de_erro = encontrar_taxa_de_erro(camada_resultado,resultado)
print('a taxa de erro é ',taxa_de_erro)