import array as arr
import numpy as np

numeros_ar = arr.array("d", [1, 3.5]) # d - double
# numeros_ar = arr.array("d", [1, 3.5, "Matheus"]) - não é possivel adc str
print(numeros_ar)

numero = np.array([1, 3.5])
print(numero)
print(numero + 3) # soma em todos os itens

