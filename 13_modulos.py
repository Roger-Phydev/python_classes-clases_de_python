### Modulos ###
#Un modulo es similar al concepto de paquete o librería en otros lenguajes de programación como C o Java.
#su mayor utilidad es utilizar menos líneas de código, asi como reciclar código, o evitar redundancias.
# previamente hemos creado una función llamada my_function, pero si la usamos en este fichero no lo reconocerá.
#eso se soluciona usando modulos.
import modulo_estadistica #aquí importamos lo que contiene el fichero modulo_estadística, para que funcione NO DEBE INICIAR CON NÚMERO
A = [1,1,3,4,4,2,1,3,4,2]
print(modulo_estadistica.calculate_mean(A)) #para usar funciones debemos considerarlo como un método, por ello ponemos un "."
print(modulo_estadistica.calculate_std(A))
from modulo_estadistica import calculate_mean,calculate_std #aquí solo importa la función en concreto
print(calculate_mean(A)) #cuando se importan funciones en específico, ya no se usan como métodos
print(calculate_std(A))
#Existen un montón de módulos que Python ya tiene por defecto, pero que no están habilitadas desde el inicio, sino que debemos importarlos.
import math, random #por ejemplo estos modulos
print(math.pi) #este modulo tiene el valor de pi, por ejemplo, cosa que por defecto no existe.
print(random.random()) #esto elige un número al azar entre 0 y 1
print(math.pow(2,3)) #esto es equivalente a  2**3
from math import pi as Pi_value #aquí renombramos lo importado
print(Pi_value)