### manejo de errores ###
# los programas siempre estarán sujetos a errores, por ello es necesario aprender a manejarlos.
#Para controlar errores se usa el código "try:","except:","else:" y "finally:".
#si ocurre un error en try, salta a except, sino va por else e independientemente de lo anterior, pasas a finally.
"""
number_one, number_two = 5 , 1      #supongamos que tenemos estos valores
number_two = "1"         #en algún momento este pasa a ser texto
print(number_one+number_two)          #eso rompe esta parte

if type(number_one) and type (number_two): #esto podría solucionar el problema, pero esto se conoce como criterio de aceptación
fdsdgthgtrgt    #hacer eso es solo posible si se conoce la raíz del problema. Veamos ahora la solución:
"""
number_one, number_two = 5, 1
number_two = "1"
try:
    print(number_two + number_one)
    print("no ha habido error")
except TypeError: #hay diferentes tipos de excepciones, aqui solo se ejecuta si hay error de tipo
    #otros tipos de errores son "ValueError", "TabError", etc. Si no se coloca nada, buscara entre todos los posibles errores.
    print("ocurrió un error") #en caso de error, el programa no se detiene.
else:
    print("La ejecución continúa correctamente")#esto solo aparece cuando no se ejecuta except y se ejecuta después del código de try
finally: #este se ejecuta SIEMPRE
    print("La ejecución continúa") 
#en lo anterior, no es necesario poner else o finally, try y except son NECESARIOS.

try:
    print(number_one + number_two)
except TypeError as error:#aquí error captura información de la falla
    print(error) #se puede aprovechar para dar información sobre el error que ocurrió
except ValueError as error: #se puede agregar más tipos de error para abarcar varios casos
    print(error)
