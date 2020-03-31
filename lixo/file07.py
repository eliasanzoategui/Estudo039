import file08
import random

txt = 'é um número par?'

n1 = file08.neuro('aleatório','aleatório','aleatório',10,0.7,0.7,1.5,0)

for i in  range(0,50000):
    n1.exercício(1,False)
    n1.exercício(2,True)
    n1.exercício(3,False)
    n1.exercício(4,True)
    n1.exercício(5,False)
    n1.exercício(6,True)
    n1.exercício(7,False)
    n1.exercício(8,True)
    n1.exercício(9,False)
    n1.exercício(10,True)

n1.execução(5,'é um número par','é um número impar')