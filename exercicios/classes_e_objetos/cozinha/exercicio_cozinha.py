# importação simples

import prato
import detergente
import garrafa


# declarando as classes

prato1 = prato.Prato('prato1',300)
prato1.cor('verde')
prato2 = prato.Prato('prato2',250)
prato2.cor('azul')
prato3 = prato.Prato('prato3',350)
prato3.cor('amarelo')
garrafa1 = garrafa.Garrafa('garrafa1')
garrafa1.volume(500)
pratos = [prato1,prato2,prato3]
detergente_multiuso = detergente.Detergente(250)

# declarando as funções



def encher_prato(prato):
    prato.encher_prato()
def esvaziar_prato(prato):
    prato.esvaziar_prato()
def limpar_prato(prato,detergente):
    if prato.estálimpo:
        print('o ',prato.nome,' já está limpo')
    else:
        d1 = detergente.litros  / prato.volume
        d1 *= 10
        if detergente.litros - d1 >= 0:
            detergente.litros -= d1
            if not prato.estácheio:
                 prato.limpo()
            else:
                print('o ',prato.nome,' está cheio')
        else:
            detergente.litros -= d1
            prato.limpo()
            print('acabou o detergente')
def encher_garrafa(garrafa):
    if garrafa.estácheio:
        if garrafa.estálimpo:
            print('a ',garrafa.nome,' já está cheia')
        else:
            print('a ',garrafa.nome,' está suja')
    else:
        if garrafa.estálimpo:
            garrafa.encher_garrafa()
def esvaziar_garrafa(garrafa):
    garrafa.esvaziar_garrafa()
def tomar_café(garrafa):
    if not garrafa.estácheio:
        if not garrafa.estálimpo: 
            print('a ',garrafa.nome,' está suja e vazia')
        if garrafa.estálimpo:
            print('a ',garrafa.nome,' está vazia')
            
    else:
        garrafa.esvaziar_garrafa()
        print('uhmmmm, muito gostoso')
    
def limpar_garrafa(garrafa,detergente):
    if garrafa.estácheio:
        print('a ',garrafa.nome,' está cheia')
    else:
        d1 = detergente.litros / garrafa.volume
        d1 *= 10
        if detergente.litros - d1 >= 0:
            detergente.litros  -= d1
            garrafa.limpar_garrafa()
        else:
            detergente.litros  -= d1
            garrafa.limpar_garrafa()
            print('acabou o detergente')

# texto explicativo

print(' digite uma ação e depois precione enter: ')
print('para mostrar todos os comandos, digite mostrar comandos.')

# lista de funções

lista_de_função = ['mostrar pratos limpos','mostrar pratos sujos','mostrar detergente','encher prato1','encher prato2'
,'encher prato3','limpar prato1','limpar prato2','limpar prato3','esvaziar prato1',
'esvaziar prato2','esvaziar prato3','encher garrafa1','tomar café',
'esvaziar garrafa1','limpar garrafa1','mostrar garrafa1']
a = 0

# sequência de comandos
while a != 'fechar':
    a = input('digite o comando: ')
    if 'comando' in a:
        for i in lista_de_função:
            print('>>',i)
        print('Você pode encher,limpar e esvaziar os pratos e a garrafa, para fazer isso digite e precione enter ')
    if a == 'mostrar pratos limpos':
        for i in pratos:
            if i.estálimpo:
                print(i.nome,'está limpo')
    if a == 'mostrar pratos sujos':
        for i in pratos:
            if not i.estálimpo:
                print(i.nome,' está sujo')
    if a == 'mostrar detergente':
        print(detergente_multiuso.litros)
    if a == 'encher prato1':
        encher_prato(prato1) 
    if a == 'encher prato2':
      encher_prato(prato2)
    if a == 'encher prato3':
        encher_prato(prato3)
    if a == 'limpar prato1':
        limpar_prato(prato1,detergente_multiuso)
    if a == 'limpar prato2':
        limpar_prato(prato2,detergente_multiuso)
    if a == 'limpar prato3':
        limpar_prato(prato3,detergente_multiuso)
    if a == 'esvaziar prato1':
        esvaziar_prato(prato1)
    if a == 'esvaziar prato2':
        esvaziar_prato(prato2)
    if a == 'esvaziar prato3':
        esvaziar_prato(prato3)
    if a == 'encher garrafa1':
        encher_garrafa(garrafa1)
    if a == 'tomar café':
        tomar_café(garrafa1)
    if a == 'esvaziar garrafa1':
        esvaziar_garrafa(garrafa1)
    if a == 'limpar garrafa1':
        limpar_garrafa(garrafa1,detergente_multiuso)
    if a == 'mostrar garrafa1':
        if garrafa1.estácheio:
            print('a garrafa1 está cheia')
        else:
            print('a garrafa1 está vazia')

    
    
    
    
    
    
    
