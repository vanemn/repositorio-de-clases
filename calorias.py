

#El programa debe solicitar al usuario la cantidad de gramos de proteína, carbohidratos y grasa; calcular las calorías usando la fórmula
#variables
# import math
# proteina = 1.9
# carbohidratos = 9.2
# grasa = 7

# calorias = 4 * (proteina + carbohidratos) + 9 * grasa
#\text{calorías} = 4 \times (\text{proteína} + \text{carbohidratos}) + 9 \times \text{grasa}
# calorias = 4 * (proteina + carbohidratos) + 9 * grasa

# print(calorias)
# print(calorias % 1 > 0)




#calorıˊas=4×(proteıˊna+carbohidratos)+9×grasa; redondear las calorías hacia arriba, y finalmente imprimir el resultado en el formato: "Las calorías totales del producto son: <calorías redondeadas>".
#El programa debe solicitar al usuario la cantidad de gramos de proteína, carbohidratos y grasa; calcular las calorías usando la fórmula \( \text{calorías} = 4 \times (\text{proteína} + \text{carbohidratos}) + 9 \times \text{grasa} \); redondear las calorías hacia arriba, y finalmente imprimir el resultado en el formato: "Las calorías totales del producto son: <calorías redondeadas>".

import math
proteina = float(input("Ingrese los gr de proteínas: \n"))
carbohidratos = float(input("Ingrese los gr de carbohidratos: \n"))
grasa = float(input("Ingrese los gramos de grasas: \n"))

# calorias = 4 * (proteina + carbohidratos) + 9 * grasa
calorias = 4 * (proteina + carbohidratos) + 9 * grasa
calorias = math.ceil(calorias)

#print(f'Las calorías totales del producto son: {math.ceil(calorias)}')
print(f'Las calorías totales del producto son: {calorias}')
