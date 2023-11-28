import numpy as np

simple_array = np.array([1,2,3])
matriz = np.array([[1,2,3],[4,5,6]])
#print [[1 2 3]
#       [4 5 6]]

# primeiro parâmetro são o número de linhas
# o segundo são o número de colunas
zeros_array = np.zeros((2,3))
#print [[0. 0. 0.]
#       [0. 0. 0.]]

#primeiro número inicial
#segundo número total
#terceiro espaços entre os números
range_array = np.arange(0,10,3)
#print [0 3 6 9]

## Operações com arrays


arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

result = arr1 + arr2
# print(result)
result = arr1 * arr2
# print(result)


# indexação e Fatiamento

# Indexação
element = arr1[0]
#print(element)
#Primeiro numero a linha e o segundo a coluna
element = arr2[0, 2]
#print(element)

# Fatiamento
subset = arr1[1:]
#print(subset)
subset = arr2[:, 2]
print(subset)
