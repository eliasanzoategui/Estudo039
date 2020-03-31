import random
import file09

n1 = file09.neu(5,0,0,random.random())

for i in range(0,10000):
    num = random.randint(0,10)
    if num == 0 or num == 2 or num == 4 or num == 6 or num == 8 or num == 10:
        n1.teste(num,True)
    else:
        n1.teste(num,False)

n1.execução(10,'é um número par','é um número impar')