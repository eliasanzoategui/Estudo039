import random

def ativar(neuronios,entrada,limiar):
    x = 0
    for i in neuronios:
        x += entrada*i['peso']+i['bias']
    if x <= limiar:
        return 0
    else:
        return x

def ajustes(neuronios,taxa_de_erro):
    x = 0
    for i in neuronios:
        x += 1
    return taxa_de_erro/x
    




valor1 = 2
valor2 = -2
valor3 = 1
valor4 = -1
valor_de_entrada = float(input('digite a entrada: '))

neuronio1_da_camada1 = {'peso':random.random(),'bias':random.random()}
neuronio2_da_camada1 = {'peso':random.random(),'bias':random.random()}
neuronio3_da_camada1 = {'peso':random.random(),'bias':random.random()}
neuronio4_da_camada1 = {'peso':random.random(),'bias':random.random()}

camada1 = [neuronio1_da_camada1,neuronio2_da_camada1,neuronio3_da_camada1,neuronio4_da_camada1]
valor_da_camada1 = ativar(camada1,valor_de_entrada,0)
print(valor_da_camada1)

neuronio1_da_camada2 = {'peso':random.random(),'bias':random.random()}
neuronio2_da_camada2 = {'peso':random.random(),'bias':random.random()}
neuronio3_da_camada2 = {'peso':random.random(),'bias':random.random()}
neuronio4_da_camada2 = {'peso':random.random(),'bias':random.random()}

camada2 = [neuronio1_da_camada2,neuronio2_da_camada2,neuronio3_da_camada2,neuronio4_da_camada2]
valor_da_camada2 = ativar(camada2,valor_da_camada1,0)
print(valor_da_camada2)

neuronio1_da_camada3 = {'peso':random.random(),'bias':random.random()}
neuronio2_da_camada3 = {'peso':random.random(),'bias':random.random()}
neuronio3_da_camada3 = {'peso':random.random(),'bias':random.random()}
neuronio4_da_camada3 = {'peso':random.random(),'bias':random.random()}

camada3 = [neuronio1_da_camada3,neuronio2_da_camada3,neuronio3_da_camada3,neuronio4_da_camada3]
valor_da_camada3 = ativar(camada3,valor_da_camada2,0)
print(valor_da_camada3)


valor_de_saida = valor_da_camada3
resultado = float(input('digite o resultado: '))
taxa_de_erro = valor_de_saida - resultado


taxa_de_erro_da_camada3 = ajustes(camada3,taxa_de_erro)
taxa_de_erro_da_camada2 = ajustes(camada2,taxa_de_erro_da_camada3/2)
taxa_de_erro_da_camada1 = ajustes(camada1,taxa_de_erro_da_camada2/2)

for i in camada3:
    numero_aleatorio = random.randint(0,1)
    if numero_aleatorio == 1:
        i['bias'] += taxa_de_erro_da_camada3
    else:
        i['bias'] -= taxa_de_erro_da_camada3
    numero_aleatorio = random.randint(0,1)
    if numero_aleatorio == 1:
        i['peso'] += (taxa_de_erro_da_camada3/100)*5
    else:
        i['peso'] -= (taxa_de_erro_da_camada3/100)*5

for i in camada2:
    numero_aleatorio = random.randint(0,1)
    if numero_aleatorio == 1:
        i['bias'] += taxa_de_erro_da_camada2
    else:
        i['bias'] -= taxa_de_erro_da_camada2
    numero_aleatorio = random.randint(0,1)
    if numero_aleatorio == 1:
        i['peso'] += (taxa_de_erro_da_camada2/100)*5
    else:
        i['peso'] -= (taxa_de_erro_da_camada2/100)*5

for i in camada1:
    numero_aleatorio = random.randint(0,1)
    if numero_aleatorio == 1:
        i['bias'] += taxa_de_erro_da_camada1
    else:
        i['bias'] -= taxa_de_erro_da_camada1
    numero_aleatorio = random.randint(0,1)
    if numero_aleatorio == 1:
        i['peso'] += (taxa_de_erro_da_camada1/100)*5
    else:
        i['peso'] -= (taxa_de_erro_da_camada1/100)*5