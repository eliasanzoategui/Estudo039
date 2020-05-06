'''
Usei um vídeo para fazer essa classe. Está em Inglês (https://www.youtube.com/watch?v=kft1AJ9WVDk)

Sua tarefa é:
- Traduzir o nome das variáveis para português.
- Traduzir o nome das funções para português.
- Comentar, acima das funções, o que cada função é.
- Escolher dois alimentos da sua cozinha e testar se eles funcionam na rede neural ou não. Um dos alimentos tem que ser um macarrão.
'''
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def normalizer(x):
    if(x <= 0.5):
        return 0
    else:
        return 1

def sigmoid_derivative(x):
    return x * (1 - x)

'''
Objetivo: identificar o que é macarrão ou não com base nos valores de calorias, gordura, carboidratos e proteína

Alimento          Calorias Gordura  Carboidratos  Proteina
Granola	            293      14.4      32           8.9
Flocos de Cereais   96       0.7       24.1         2.8
Flocos de milho     100      0.01      22.2         1.9
Macarrão cru        390      1.6       78.4         13.7
Molho de tomate     71       0.4       16.4         3.2
Macarrão Integral   365      1.5       78.8         15.4
Macarrão Japonês    366      0.7       74.6         14.4

Calorias
< 200     => -1
200 - 300 => 0
>300      => 1

Gordura
>2       => -1
2 - 0.7  => 0
< 0.7    => 1

Carboidratos
<30      => -1
30 - 60  => 0
> 60     => 1

Proteina
< 6      => -1
6 - 12   => 0
> 12     => 1
'''

training_inputs = np.array([[ 0, -1,  0,  0],
                            [-1,  0, -1, -1],
                            [-1,  1, -1, -1],
                            [ 1,  1,  1,  1],
                            [ 1,  0,  1,  1]])

training_outputs = np.array([[0,0,0,1,1]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((4, 1)) - 1

print('Synaptic weights initialized')
print(synaptic_weights)

for iteration in range(1):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    error = training_outputs - outputs
    adjustments = error * sigmoid_derivative(outputs)
    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Synaptic Weights: ')
print(synaptic_weights)

print('outputs:')
print(outputs)

test_input = np.array([[-1, 0, -1, -1],
                       [ 1, 0,  1,  1]])
final_output = sigmoid(np.dot(test_input, synaptic_weights))

print('Final Output: ')
print(final_output)

for a in outputs:
    print(normalizer(a))

for a in final_output:
    print(normalizer(a))