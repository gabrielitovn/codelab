
#Crear un nuevo repositorio en tu Github para alamcenar este y sucesivos proyectos del curso
#Crea un nuevo archivo .py
#Define una variable de cada tipo de primitivo
#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
#Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo
#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
#Imprimir los resultados de las tareas anteriores
#Envía el link del archivo en el repositorio con las respuesta
# Definir variables de diferentes tipos primitivos
cadena = "Hola, soy una cadena"
entero = 42
flotante = 3.14159
hombre = True
paso_2 = str(cadena) + str(entero) + str(hombre) + str(flotante)
print(paso_2)
# Investigación sobre los límites de enteros y flotantes en Python
# Python no tiene límites estrictos para enteros, pero la cantidad máxima depende de la memoria disponible en tu sistema.
# Los flotantes siguen el estándar IEEE 754, y tienen límites definidos, como el máximo valor representable con `sys.float_info.max`.
# Calcular la suma de los primeros n números pares (investigar)
# La suma de los primeros n números pares se puede calcular con la fórmula: n * (n + 1)
n = int(input())
suma_numeros_pares = n * (n + 1)
print(suma_numeros_pares)

