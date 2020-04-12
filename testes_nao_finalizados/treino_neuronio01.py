import testes_com_neuronios04

neuronio1 = testes_com_neuronios04.neuronio(0,0,0.5,0.5)
neuronio2 = testes_com_neuronios04.neuronio(0,0,0.5,0.5)
neuronio1.neuronio_de_anexo(neuronio2)
neuronio3 = testes_com_neuronios04.neuronio(0,0,0.5,0.5)
neuronio2.neuronio_de_anexo(neuronio3)
neuronio4 = testes_com_neuronios04.neuronio(0,0,0.5,0.5)
neuronio3.neuronio_de_anexo(neuronio3)

neuronios = [neuronio1,neuronio2,neuronio3,neuronio4]


for i in neuronios:
    i.treino([0],1)
    i.treino([1],0)
    i.treino([2],1)
    i.treino([3],0)
    i.treino([4],1)
    i.treino([5],0)
    i.treino([6],1)
    i.treino([7],0)
    i.treino([8],1)
    i.treino([9],0)
    i.treino([10],1)

neuronio1.teste(2,'é par','é impar')

