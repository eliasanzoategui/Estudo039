import estrutura_neuronio
import random

txt = 'é um número par?'

n1 = estrutura_neuronio.neuronio('aleatório','aleatório','aleatório',10,0.7,0.7,1.5,0)

for i in range(0,50000):
    n1.exercicio(1,False)
    n1.exercicio(2,True)
    n1.exercicio(3,False)
    n1.exercicio(4,True)
    n1.exercicio(5,False)
    n1.exercicio(6,True)
    n1.exercicio(7,False)
    n1.exercicio(8,True)
    n1.exercicio(9,False)
    n1.exercicio(10,True)

n1.execucao(5,'é um número par','é um número impar')
