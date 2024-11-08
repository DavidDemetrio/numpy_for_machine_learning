# import matplotlib.pyplot as plt
import numpy as np

lista = [31,28,29,19]

# Esto se almacena en memoria
arr = np.array(lista)

# print(lista)
# print(arr)

""" Ejercicio 3 """
lista_2d=[[2,3,4],
          [3,4,5],
          [3,4,5],
          [3,4,5]]

arr_2d = np.array(lista_2d)
# print(arr_2d)

lista_distinct_data=[[2,"data1",False],
                     [2.34, False, "data2"]]

arr_distinct_data = np.array(lista_distinct_data)

print("list_distinct_data: ", lista_distinct_data)
print("arr_distinct_data: ", arr_distinct_data)

""" Ejercicio 4 """
print(arr_2d.shape) # tamaño del arreglo array arr_2d
print(arr.shape) # tamaño del arreglo arr
# NOTA: shape es útil cuando tienes dimensiones de arreglos muy grandes

# Saber el tipo de dato que tiene el arreglo
print(arr.dtype)
print(arr_2d.dtype)

""" 
Nota: Cuando tienes un array de n dimenciones, donde los datos
pueden ser de cualquier tipo, numpy transforma estos datos a un
solo tipo, en este caso el más conveniente es el tipo string.
"""
print("arr_distinct_data.dtype: ", arr_distinct_data.dtype)

"""
Si deseas mantener la heterogeniedad en los datos del arreglo,
puedes especificar el tipo object en la lista.
"""
list_diff_data = [[34,"data4",False],
                  [False, 45, "data6"]]
arr_diff_data = np.array(list_diff_data, dtype=object)
print("types data into array: ", arr_diff_data.dtype)
""" 
    El contra de mantener la integridad del tipo de dato en el array
    es en el rendimiento en como numpy operará los datos, ya que es más
    facil al tener todos los datos en el tipo string
 """

""" Ejercicio 5 """
# Especificar el tipo de dato al crear un array
arr3 = np.array(lista_2d, dtype=np.int32)
print("arr3", arr3)

# Numpy para machine learning
""" Ejercicio 6 """
# Crear matrices con datos y tamaño por default
# para test de modelos de machine learning
matriz_default = np.zeros((3,2)) # crea una matriz por default llena de zeros
print("matriz_default: ", matriz_default)

matriz_default_ones = np.ones((4,4))
print("matriz_default_ones: ", matriz_default_ones)